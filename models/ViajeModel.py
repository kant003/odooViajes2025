from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class Viaje(models.Model):
    _name = 'viajes.viaje'
    _description = "Viajes"

    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")
    finalizado = fields.Boolean(default=False)

    estado = fields.Selection(
        selection=[
            ('planeado', 'Planeado'),
            ('en_curso', 'En curso'),
            ('finalizado', 'Finalizado')
        ],
        string="Estado",
        default="planeado",
        required=True
    )

    # En la relación many2one me permite elegir un partner/cliente o crear uno directamente
    # Tener en cuenta que solo aparecerán los partners/clientes que sean de tipo conductor
    conductor_id = fields.Many2one('res.partner', string="Conductor", domain=[('conductor', '=', True)])

    # En la relación many2one me permite elegir un vehiculo o crear uno directamente
    vehiculo_id = fields.Many2one('viajes.vehiculo',
        ondelete='cascade', string="Vehiculo", required=True)
    

    # puedo elegir uno(partner/cliente) que ya existe o crear uno nuevo
    pasajeros_ids = fields.Many2many('res.partner', string="Pasajeros")

    plazas_ocupadas = fields.Float(string="Plazas ocupadas", compute='_get_plazas_ocupadas')

    @api.depends('plazas', 'pasajeros_ids')
    def _get_plazas_ocupadas(self):
        for r in self:
            if not r.plazas:
                r.plazas_ocupadas = 0.0
            else:
                r.plazas_ocupadas = 100.0 * len(r.pasajeros_ids) / r.plazas

    
    fecha_fin = fields.Date(compute="_compute_fecha_fin")

    @api.depends('fecha_inicio', 'duracion')
    def _compute_fecha_fin(self):
        for record in self:
            if record.fecha_inicio and record.duracion:
                record.fecha_fin = record.fecha_inicio + timedelta(days=record.duracion)


    estado_display = fields.Char(compute="_compute_estado_display")

    @api.depends('estado')
    def _compute_estado_display(self):
        estados_dict = {'planeado': '⏳ Planeado', 'en_curso': '🚀 En Curso', 'finalizado': '✅ Finalizado'}
        for record in self:
            record.estado_display = estados_dict.get(record.estado, 'Desconocido')



    # Añade onchange explícito para advertir sobre valores no válidos, como un número negativo de plazas o más pasajeros que plazas
    @api.onchange('plazas', 'pasajeros_ids')
    def _checkearPlazasValidas(self):
        if self.plazas < 0:
            self.plazas = 0
            return {
                'warning': {
                    'title': "Valor de 'plazas' incorrecto",
                    'message': "El numero de plazas disponibles no puede ser negativo",
                },
            }
        if self.plazas < len(self.pasajeros_ids):
            return {
                'warning': {
                    'title': "Demasiados pasajeros",
                    'message': "Incrementa el nº de plazas o elimina pasajeros",
                },
            }
        


    @api.constrains('conductor_id', 'pasajeros_ids')
    def _comprobarConductorNoEsPasajero(self):
        for r in self:
            if r.conductor_id and r.conductor_id in r.pasajeros_ids:
                raise ValidationError("Un conductor no puede ser también pasajero")
            

    paradas_ids = fields.One2many('viajes.parada', 'viaje_id', 
                                  string="Paradas del viaje")
    
    @api.depends('titulo')
    def _compute_display_name(self):
        for r in self:
            r.display_name = r.titulo
from odoo import fields, models, api
class Vehiculo(models.Model):
    _name = "viajes.vehiculo"
    _description = "Vehiculo Viajes"

    modelo = fields.Char(string="Modelo", required=True)
    marca = fields.Char(string="Marca")
    descripcion = fields.Text()

    #Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    propietario_id = fields.Many2one('res.users',
        ondelete='set null', string="Propietario", index=True)
    
    @api.depends('modelo', 'marca')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.modelo} - {record.marca}" if record.marca else record.modelo


    viaje_ids = fields.One2many('viajes.viaje', 'vehiculo_id', string="Viajes del coche")
    
    
    matricula = fields.Char()

    _sql_constraints = [
        ('matricula_descripcion_check',
         'CHECK(matricula != descripcion)',
         "La matricula del coche no puede ser igual que la descripción"),

        ('nmatricula_unique',
         'UNIQUE(matricula)',
         "La matricula tiene que ser única"),
    ]


    revision_ids = fields.One2many('viajes.revision', 'vehiculo_id', string="Revisiones del coche")
    
    
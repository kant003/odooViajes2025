from odoo import fields, models, api

class Parada(models.Model):
    _name = "viajes.parada"
    _description = "Paradas de los Viajes"

    titulo = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string="Fecha", default=fields.Date.today)
    duracion = fields.Float(digits=(5, 2), help="Duración en horas")
    localizacion = fields.Char(string="Localización")

    viaje_id = fields.Many2one('viajes.viaje', ondelete='cascade', string="Viaje", required=True)
    completada = fields.Boolean(string="Parada completada", default=False)

    @api.depends('completada')
    def marcar_completada(self):
        for record in self:
            record.completada = not record.completada

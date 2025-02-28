from odoo import fields, models

class Revision(models.Model):
    _name = "viajes.revision"
    _description = "Revisiones de los Vehiculos"

    titulo = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string="Fecha", default=fields.Date.today)
    superada = fields.Boolean(default=False)
    
    vehiculo_id = fields.Many2one('viajes.vehiculo',
        ondelete='cascade', string="Vehiculo", index=True)
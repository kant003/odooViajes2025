# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    conductor = fields.Boolean("Conductor", default=False)

    viaje_ids = fields.Many2many('viajes.viaje',
        string="Viajes realizados", readonly=True)
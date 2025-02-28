# -*- coding: utf-8 -*-
# from odoo import http


# class Viajes(http.Controller):
#     @http.route('/viajes/viajes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viajes/viajes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viajes.listing', {
#             'root': '/viajes/viajes',
#             'objects': http.request.env['viajes.viajes'].search([]),
#         })

#     @http.route('/viajes/viajes/objects/<model("viajes.viajes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viajes.object', {
#             'object': obj
#         })


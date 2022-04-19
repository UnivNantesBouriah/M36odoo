# -*- coding: utf-8 -*-
# from odoo import http


# class GestionAlternants(http.Controller):
#     @http.route('/gestion_alternants/gestion_alternants/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_alternants/gestion_alternants/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_alternants.listing', {
#             'root': '/gestion_alternants/gestion_alternants',
#             'objects': http.request.env['gestion_alternants.gestion_alternants'].search([]),
#         })

#     @http.route('/gestion_alternants/gestion_alternants/objects/<model("gestion_alternants.gestion_alternants"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_alternants.object', {
#             'object': obj
#         })

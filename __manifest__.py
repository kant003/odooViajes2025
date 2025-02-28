# -*- coding: utf-8 -*-
{
    'name': "viajes",

    'summary': "Gestor de viajes",

    'description': """
        Este módulo permite el control y gestión de los viajes que realizan pasajeros
    """,

    'author': "Angel",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Viajes',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vehiculo.xml',
        'views/viaje.xml',
        'views/partner.xml',
        'views/parada.xml',
        'views/revision.xml',
        'views/menus.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/demo.viaje.xml'
    ],
    'installable': True,
    'application': True
}


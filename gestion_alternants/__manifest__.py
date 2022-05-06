# -*- coding: utf-8 -*-
{
    'name': "GestionAlternants",

    'summary': """
        Gestion des alternants à l'IUT R&T de la Roche sur Yon""",

    'description': """
        Gestion des alternants
    """,

    'author': "IUT La Roche sur Yon département R&T",
    'website': "http://www.univ-nantes.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                ],

    # always loaded
    'data': [
        'security/gestion_alternants_security.xml',
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/gestion_alternants.xml',
#        'views/templates.xml',   
        'menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

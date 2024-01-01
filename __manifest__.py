# -*- coding: utf-8 -*-
{
    'name' : 'ContactTravel',
    'version': '17.0',
    'summary': 'Contact and travel stuff',
    'depends': ['base'],
    'data': [
        'views/voyage_views.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}

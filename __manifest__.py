# -*- coding: utf-8 -*-
{
    'name' : 'Contact Travel',
    'version': '0.0.1',
    'summary': 'Contact and travel stuff',
    'author': "Abdeldjalil Hebal",
    'website': "https://github.com/djalilhebal/contact-travel",
    'depends': ['base'],
    'data': [
        'views/voyage_views.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}

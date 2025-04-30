# -*- coding: utf-8 -*-
{
    'name' : 'optesis signature',
    'version' : '1.0',
    'author': 'Moore sn',
    'maintainer': 'Moore sn',
    'summary': 'Optesis signature',
    'sequence': 1,
    'description': """
SMS marketing 
====================
This module allow you sign your document
    """,
    'category': 'purchase',
    'website': 'https://moore.sn',
    'images' : ['images/icon.png'],
    'depends' : ['base_setup', 'purchase'],
    'data': ['views/res_users.xml', 'views/purchase_order.xml'],
    'installable': True,
    'application': True,
    'autoinstall': False,
}

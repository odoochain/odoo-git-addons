# © 2023 - Today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Github Events',
    'version': "16.0.0.0",
    'author': 'Numigi,odooChain',
    'maintainer': 'odooChain,Numigi',
    'website': 'https://bit.ly/numigi-com',
    'license': 'LGPL-3',
    'category': 'Connector',
    'summary': 'Define what is a github event as an odoo object',
    'depends': [
        'base_sparse_field',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/github_event.xml',
        'views/menu.xml',
    ],
    'installable': True,
}

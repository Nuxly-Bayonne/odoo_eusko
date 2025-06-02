{
    'name': 'Odoo Eusko',
    'version': '0.1',
    'summary': 'Intégration de la devise Eusko dans Odoo.',
    'description': """
    Ce module Odoo permet une gestion de la monnaie locale Eusko :
    
    Fonctionnalités :
    - Ajoute automatiquement la devise "Eusko" (EUS) dans le système.
    - Vérifie que la société utilise l'euro (€) avant installation.
    - Désactive la devise Eusko automatiquement lors de la désinstallation du module.
    
    Conditions :
    - Ce module ne peut être installé que si la devise principale de la société est l'euro (€).

    Public cible :
    - Sociétés basques utilisant ou acceptant les paiements en Eusko.
    
    """,
    'author': 'Nuxly Bayonne',
    'website': 'https://nuxly.com',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'depends': ['base','account'],
    'data': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': 'check_currency_euro',
    'uninstall_hook': 'deactivate_eusko_currency',
}


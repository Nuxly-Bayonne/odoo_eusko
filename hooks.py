from odoo import api, SUPERUSER_ID
from odoo.exceptions import ValidationError


def check_currency_euro(cr):
    """
    Hook de pré-initialisation pour Odoo 16.
    Vérifie que la devise principale de la société est l'euro (€).
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    company = env["res.company"].search([], limit=1)
    currency = company.currency_id

    if currency.name != "EUR":
        raise ValidationError(
            "\nInstallation bloquée :\n"
            "Ce module ne peut être installé que si la devise principale de la société est l'euro (€).\n\n"
        )


def deactivate_eusko_currency(cr, registry):
    """
    Hook de désintallation.
    Désactive la devise 'Eus' si elle existe.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    eusko = env["res.currency"].search([("name", "=", "Eus")], limit=1)
    if eusko:
        eusko.active = False

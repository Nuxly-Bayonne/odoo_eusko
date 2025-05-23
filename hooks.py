def check_currency_euro(env):
    company = env['res.company'].search([], limit=1)
    currency = company.currency_id

    if currency.name != 'EUR':
        raise Exception(
            "\nInstallation bloquée :\n"
            "Ce module ne peut être installé que si la devise principale de la société est l'euro (€).\n\n"
            )

def deactivate_eusko_currency(env):
    eusko = env['res.currency'].search([('name', '=', 'Eus')], limit=1)
    if eusko:
        eusko.active = False

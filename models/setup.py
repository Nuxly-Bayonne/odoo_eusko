from odoo import api, models

class CreateEuskoCurrency(models.AbstractModel):
    _name = 'create.eusko.currency'
    _description = "Création automatique de la devise Eusko"

    @api.model
    def init(self):
        currency_env = self.env['res.currency']

        existing = currency_env.search([('name', '=', 'Eusko')], limit=1)
        if not existing:
            currency_env.create({
                'name': 'Eus',
                'full_name': 'Eusko',
                'active': True,
                'symbol': 'EUS',
                'currency_unit_label': 'Eusko',
                'position': 'after',
                'rounding': 0.01,
                'decimal_places': 2,
            })

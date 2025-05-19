from odoo import api, models, fields
from datetime import date


class CreateEuskoCurrency(models.AbstractModel):
    _name = "create.eusko.currency"
    _description = "Création automatique de la devise Eusko"


    def init(self):
        currency_env = self.env["res.currency"]
        rate_env = self.env["res.currency.rate"]
        company = self.env.company

        # Recherche la devise EUR par son code
        euro = self.env['res.currency'].with_context(active_test=False).search(
            [('name', '=', 'EUR')], limit=1)
        if euro:
            if not euro.active:
                euro.write({'active': True})
            # Forcer l'euro comme devise principale de l'entreprise
            company.write({'currency_id': euro.id})


        # Ajouter la devise Eusko
        existing = currency_env.search([("name", "=", "Eusko")], limit=1)
        if not existing:
            currency_env.create(
                {
                    "name": "Eus",
                    "full_name": "Eusko",
                    "active": True,
                    "symbol": "EUS",
                    "currency_unit_label": "Eusko",
                    "position": "after",
                    "rounding": 0.01,
                    "decimal_places": 2,
                }
            )


        # Date personnalisée
        custom_date = fields.Date.to_date("2025-05-19")
        currency = currency_env.search([("name", "=", "Eusko")], limit=1)

        # Vérifie si le taux existe déjà pour cette date
        existing_rate = rate_env.search(
            [
                ("currency_id", "=", currency.id),
                ("name", "=", custom_date),
                ("company_id", "=", company.id),
            ],
            limit=1,
        )

        # Crée le taux s'il n'existe pas
        if not existing_rate:
            rate_env.create(
                {
                    "currency_id": currency.id,
                    "rate": 1.0,
                    "name": custom_date,
                    "company_id": company.id,
                }
            )

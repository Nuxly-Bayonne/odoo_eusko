from odoo import api, models, fields
from datetime import date


class CreateEuskoCurrency(models.AbstractModel):
    _name = "create.eusko.currency"
    _description = "Création automatique de la devise Eusko"

    def init(self):
        currency_env = self.env["res.currency"]
        rate_env = self.env["res.currency.rate"]
        company = self.env.company
        existing = currency_env.search([("name", "=", "Eus")], limit=1)

        if existing:
            # Réactiver si existante
            if not existing.active:
                existing.write({"active": True})

        else:
            # Ajouter la devise Eusko si inexistante
            currency_env.create(
                {
                    "name": "Eus",
                    "full_name": "Eusko",
                    "active": True,
                    "symbol": "Eusko",
                    "currency_unit_label": "Eusko",
                    "currency_subunit_label": "Centimes",
                    "position": "after",
                    "rounding": 0.01,
                    "decimal_places": 2,
                }
            )

        # Date personnalisée
        custom_date = fields.Date.to_date("2025-05-19")
        currency = currency_env.search([("name", "=", "Eus")], limit=1)

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

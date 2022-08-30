# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models

from .res_company import ResCompany


class SendGridSettings(models.TransientModel):
    _name = "res.config.settings"
    _inherit = ["res.config.settings", "abstract.config.settings"]
    _companyObject = ResCompany
    _prefix = "sendgrid_"

    sendgrid_api_key = fields.Char(
        string="Sendgrid API Key",
        related="company_id.sendgrid_api_key",
    )

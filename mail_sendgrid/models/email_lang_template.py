# Copyright 2016-2017 Compassion CH (http://www.compassion.ch)
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class LanguageTemplate(models.Model):
    """This class is the relation between and email_template object
    and a sendgrid_template. It allows to specify a different
    sendgrid_template for any selected language.
    """

    _name = "sendgrid.email.lang.template"

    email_template_id = fields.Many2one(
        string="E-mail Template",
        comodel_name="mail.template",
    )

    @api.model
    def _select_lang(self):
        obj_lang = self.env["res.lang"]
        languages = obj_lang.search([])
        return [(language.code, language.name) for language in languages]

    lang = fields.Selection(
        string="Language",
        selection="_select_lang",
        required=True,
    )
    sendgrid_template_id = fields.Many2one(
        string="Sendgrid Template",
        comodel_name="sendgrid.template",
        required=True,
    )

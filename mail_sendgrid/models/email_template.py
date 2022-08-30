# Copyright 2016-2017 Compassion CH (http://www.compassion.ch)
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from collections import defaultdict

from odoo import api, fields, models


class EmailTemplate(models.Model):
    _inherit = "mail.template"

    substitution_ids = fields.One2many(
        string="Substitutions",
        comodel_name="sendgrid.substitution",
        inverse_name="email_template_id",
    )
    sendgrid_template_ids = fields.One2many(
        string="Sendgrid Templates",
        comodel_name="sendgrid.email.lang.template",
        inverse_name="email_template_id",
    )

    @api.multi
    def _compute_localized_template(self):
        lang = self.env.context.get("lang", "en_US")
        for template in self:
            lang_template = template.sendgrid_template_ids.filtered(
                lambda t: t.lang == lang
            )
            if lang_template and len(lang_template) == 1:
                template.sendgrid_localized_template = (
                    lang_template.sendgrid_template_id
                )

    sendgrid_localized_template = fields.Many2one(
        string="sendgrid.template",
        compute="_compute_localized_template",
    )

    @api.multi
    def update_substitutions(self):
        for template in self:
            new_substitutions = []
            for language_template in template.sendgrid_template_ids:
                sendgrid_template = language_template.sendgrid_template_id
                lang = language_template.lang
                substitutions = template.substitution_ids.filtered(
                    lambda s: s.lang == lang
                )
                keywords = sendgrid_template.get_keywords()
                # Add new keywords from the sendgrid template
                for key in keywords:
                    if key not in substitutions.mapped("key"):
                        substitution_vals = {
                            "key": key,
                            "lang": lang,
                            "email_template_id": template.id,
                        }
                        new_substitutions.append((0, 0, substitution_vals))

            template.write({"substitution_ids": new_substitutions})

        return True

    @api.multi
    def render_substitutions(self, res_ids):
        """
        :param res_ids: resource ids for rendering the template
        Returns values for substitutions in a mail.message creation
        :return:
            Values for mail creation (for each resource id given)
         {res_id: list of substitutions values [0, 0 {substitution_vals}]}
        """
        self.ensure_one()
        if isinstance(res_ids, int):
            res_ids = [res_ids]
        substitutions = self.substitution_ids.filtered(
            lambda s: s.lang == self.env.context.get("lang", "en_US")
        )
        substitution_vals = defaultdict(list)
        for substitution in substitutions:
            values = self.render_template(substitution.value, self.model, res_ids)
            for res_id in res_ids:
                substitution_vals[res_id].append(
                    (0, 0, {"key": substitution.key, "value": values[res_id]})
                )
        return substitution_vals

# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class MailWizardInvite(models.TransientModel):
    _inherit = "mail.wizard.invite"

    contact_group_ids = fields.Many2many(
        string="Contact Group",
        comodel_name="partner_contact_group",
        relation="rel_mail_wiz_invite_2_partner_contact_group",
        column1="wizard_id",
        column2="group_id",
        copy=True,
    )

    @api.onchange(
        "contact_group_ids",
    )
    def onchange_partner_ids(self):
        self.partner_ids = [(5, 0, 0)]
        if self.contact_group_ids:
            self.partner_ids = [(6, 0, self.contact_group_ids.contact_ids.ids)]

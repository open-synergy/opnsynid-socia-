# Copyright 2015-2018 Compassion CH (http://www.compassion.ch)
# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "SendGrid",
    "version": "11.0.1.0.2",
    "category": "Social Network",
    "author": "Compassion CH, Odoo Community Association (OCA),"
    "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "website": "https://simetri-sinergi.id",
    "depends": [
        "mail_tracking",
        "configuration_helper",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
        "views/sendgrid_email_view.xml",
        "views/sendgrid_template_view.xml",
        "views/mail_compose_message_view.xml",
        "views/email_template_view.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "external_dependencies": {
        "python": ["sendgrid"],
    },
}

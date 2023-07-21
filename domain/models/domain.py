from odoo import fields, models

class Domain(models.Model):
    _name = "domain.domain"
    _description = "List of domains"

    name = fields.Char(string = "Title", required=True)
    active = fields.Boolean(string="Active", default=True) 
from odoo import fields, models

from odoo.addons.test_impex.models import field


class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    name = fields.Char()
    width = fields.Float()
    height = fields.Float()
    length = fields.Float()
    maximum_weight = fields.Float()




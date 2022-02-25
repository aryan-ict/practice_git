# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class smart_view(models.Model):
    _name = "smart.view"

    _description = "Model for Smart View"

    name = fields.Char(string="Name")
    phone_no = fields.Char(string="Phone Number")
    dob_id = fields.Date(string="Date Of Birth")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name is already in the database."),
    ]

    def smart_button(self):
        print("hello")

    # @api.constrains('name')
    # def check_name(self):
    #     for rec in self:
    #         if rec.name.isalpha() == False:
    #             raise ValidationError("Name must contain only alphabets")

    # @api.constrains('phone_no')
    # def check_number(self):
    #     for record in self:
    #         if len(record.phone_no) > 10 or len(record.phone_no) < 10:
    #             raise ValidationError("The number must be 10 digits long")
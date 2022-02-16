# -*- coding: utf-8 -*-

from odoo import models, fields, api


class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'), ('option2', 'Post Graduation')],string="Degree Type")
    dob = fields.Date(string="Date Of Birth")


    def sample_button_d(self):
        print("Sample Button")


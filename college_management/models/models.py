# -*- coding: utf-8 -*-

from odoo import models, fields, api


class college_management(models.Model):
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'

    name = fields.Char()
    value = fields.Integer(string="Sr Number", default=None)
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'), ('option2', 'Post Graduation')],string="Degree Type")
    dob = fields.Date(string="Date Of Birth")
    status = fields.Selection([('O1', 'Draft'), ('O2', 'Confirm'), ('O3', 'Done'), ('O4', 'Cancelled')], default='O1',
                              string="Status")

    def sample_button_d(self):
        print("Sample Button")


from odoo import models, fields, api

class College_Management(models.TransientModel):
    _name = 'college.wizard'
    _description = 'Wizard1'
    name = fields.Many2one("res.partner", string="Name")
    mobile = fields.Integer(string="Mobile Number")
    address = fields.Text(string="Address")

    def submit_button(self):
        print("Submit Button")
    def cancel_button(self):
        print("Cancel Button")

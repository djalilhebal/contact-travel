# -*- coding: utf-8 -*-

from odoo import fields, models, _

class Voyage(models.Model):
    _name = 'contact_travel.voyage'

    nom = fields.Char(string="Nom du voyage")
    date_depart = fields.Date(string="Date depart")
    destination = fields.Char(string="Destination")
    prix = fields.Float(string="Prix (DA)")
    contact_id = fields.Many2one("res.partner", string="Contact")

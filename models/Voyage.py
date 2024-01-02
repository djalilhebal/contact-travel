# -*- coding: utf-8 -*-

from odoo import fields, models, _

class Voyage(models.Model):
    _name = 'contact_travel.voyage'

    nom = fields.Char(string="Nom du voyage", required=True)
    date_depart = fields.Date(string="Date depart", required=True)
    destination = fields.Char(string="Destination", required=True)
    prix = fields.Float(string="Prix (DA)", required=True)
    contact_id = fields.Many2one("res.partner", string="Contact", required=True)

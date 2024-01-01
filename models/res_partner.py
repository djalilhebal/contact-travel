# -*- coding: utf-8 -*-

from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyages = fields.One2many('contact_travel.voyage', 'contact_id', string='Voyages')

    def action_view_partner(self):
        return {
            'name': 'List voyages',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'contact_travel.voyage',
            'domain': [('id', 'in', self.voyages.ids)]
        }

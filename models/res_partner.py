# -*- coding: utf-8 -*-

from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyages = fields.One2many('contact_travel.voyage', 'contact_id', string='Voyages')

    voyages_count = fields.Integer(string='Nombre de Voyages', compute='_count_voyages')

    def action_view_partner(self):
        return {
            'name': 'List voyages',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'contact_travel.voyage',
            'domain': [('id', 'in', self.voyages.ids)]
        }

    def _count_voyages(self):
        for record in self:
            record.voyages_count = len(record.voyages)

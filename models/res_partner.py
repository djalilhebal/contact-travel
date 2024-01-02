# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyages = fields.One2many('contact_travel.voyage', 'contact_id', string='Voyages')

    voyages_count = fields.Integer(string='Nombre de Voyages', compute='_count_voyages')

    # Reward level
    niv_recomp = fields.Selection(
        selection=[
            ('argent', 'Argent'),
            ('or', 'Or'),
            ('platine', 'Platine'),
        ],
        string='Niveau de récompense',
        default='argent',
        compute='_niv_recomp',
    )
    # The total trip expenses for the contact, used to in the calculation of the reward level.
    total_voyage_depense = fields.Float(string='Dépenses totales des voyages (DA)', compute='_total_voyage_depense')

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

    # This method triggers whenever `total_voyage_depense` changes to automatically update the reward level.
    @api.depends('total_voyage_depense')
    def _niv_recomp(self):
        for contact in self:
            if contact.total_voyage_depense >= 100_000:
                contact.niv_recomp = 'platine'
            elif contact.total_voyage_depense >= 50_000:
                contact.niv_recomp = 'or'
            else:
                contact.niv_recomp = 'argent'

    # This method triggers whenever `voyages_count` or `voyages.prix` changes to automatically update `total_voyage_depense`.
    # Why depend on `voyages_count`? To comply with the requirement:
    # "Ce niveau de récompense doit être mis à jour chaque fois qu'un nouveau voyage est associé à un client."
    @api.depends('voyages_count', 'voyages.prix')
    def _total_voyage_depense(self):
        for contact in self:
            total_depense = sum(contact.voyages.mapped('prix'))
            contact.total_voyage_depense = total_depense

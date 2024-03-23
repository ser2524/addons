from odoo import _, api, fields, models


class Lotes(models.Model):
    _name = 'Lotes'
    _description = 'Lotes'
    nombre_lote = fields.Char(string='')
    

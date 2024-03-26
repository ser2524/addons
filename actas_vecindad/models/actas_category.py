from odoo import _, api, fields, models



class Tipo_Uso(models.Model):
    _name = 'tipo_uso'
    _description = 'Tipo Uso vivienda '
    name = fields.Char(string='Tipo')
    

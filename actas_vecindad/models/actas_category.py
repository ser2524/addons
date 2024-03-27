from odoo import _, api, fields, models



class Tipo_Uso(models.Model):
    _name = 'tipo_uso'
    _description = 'Tipo Uso vivienda '
    name = fields.Char(string='Tipo')
    


class encargado(models.Model):
    _name = 'encargado'
    _description = 'encargado'
    name = fields.Char(string='Observaciones')
    
    
    

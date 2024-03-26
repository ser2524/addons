from odoo import _, api, fields, models

class Model_Main_Agro(models.Model):
    _name = 'main_agro'
    _description = 'model.technical.name'
    name = fields.Char(string='lote')
    fecha_fertilizacion = fields.Date('fecha_fertilizacion')
    active = fields.Boolean(string='es activo')
    obreros_requeridos = fields.Integer(string='Numero de Obreros')
    
    
    
    
    
    
    

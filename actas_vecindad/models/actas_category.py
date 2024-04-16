from odoo import _, api, fields, models



class Tipo_Uso(models.Model):
    _name = 'tipo_uso'
    _description = 'Tipo Uso vivienda '
    name = fields.Char(string='Tipo')
    


class encargado(models.Model):
    _name = 'encargado'
    _description = 'encargado'
    name = fields.Char(string='Observaciones')



class imagenes(models.Model):
    _name = 'imagenes_binario'
    _description = 'imagenes' 
    name = fields.Char(string='')
    _inherit =['image.mixin']       
    actas = fields.Binary(
        string='actas',            
    )
    

class usuarios_actas_id(models.Model):
      _inherit = 'res.partner'
      usuarios_actas_id = fields.Char(string='name', copy=False   )



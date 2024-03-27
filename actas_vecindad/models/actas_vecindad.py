
from odoo import _, api, fields, models

class actas(models.Model):
    _inherit =['image.mixin']# este es un modelo heredado para almacenar imágenes
    _name = 'actas_vecindad'
    _description = 'Actas de vecindad'
    name = fields.Char(string='Actas')
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario') #EL CMODEL ES EL LLAMADO DEL CAMPO   
    fecha_acta = fields.Date(string='Fecha Acta')
    numero_obreros = fields.Integer(string='Numero Obreros')
    tipo_uso = fields.Many2one(comodel_name='tipo_uso', string='Tipo De Uso') 
    encargado = fields.Many2many(comodel_name='encargado')            
    calificacion= fields.Selection(string='Calificación', selection=[('alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo'),])
    active = fields.Boolean(string='es activo', default = True)
    notas_estado = fields.Text(string='Estado Inmueble') 
    afectacion = fields.Integer('Afectación',related='afectacion_view')
    afectacion_view = fields.Integer('Afectación')
    conflicto = fields.Boolean(string ='¿Es Usuario conflictivo?')
    documento = fields.Binary(string='Documento')
    valor_inmueble = fields.Float(string='Valor Comercial')
    
    
     
    
    
   

    
    
    
    
    
    
    
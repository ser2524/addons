
from odoo import _, api, fields, models

class actas(models.Model):
    _inherit =['image.mixin']# este es un modelo heredado para almacenar imágenes
    _name = 'actas_vecindad'
    _description = 'Actas de vecindad'
    name = fields.Char(string='Actas')
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario') #EL CMODEL ES EL LLAMADO DEL CAMPO
    #para filtra el modulo
    encargado_user = fields.Many2one(comodel_name='res.partner.category', string='Usuarios Encargado' , default=lambda self : self.env['res.partner.category'].search([('name','=','Sociales')])                                     
)
    #asina valores por defecto , se usua funciones lambda
    fecha_acta = fields.Date(string='Fecha Acta')
    numero_obreros = fields.Integer(string='Numero Obreros')
    tipo_uso = fields.Many2one(comodel_name='tipo_uso', string='Tipo De Uso')
    encargado = fields.Many2many(comodel_name='encargado')
    calificacion= fields.Selection(string='Calificación', selection=[('alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo'),])
    active = fields.Boolean(string='es activo', default = True)
    notas_estado = fields.Text(string='Estado Inmueble')
    afectacion = fields.Integer('Afectación',related='afectacion_view')
    #SE CRE RELACIÓN PARA PERMITIR EDITAR EN otro campo, con related
    afectacion_view = fields.Integer('Afectación')
    conflicto = fields.Boolean()
    documento = fields.Binary(string='Documento') 
    #para conservaer el nombre se los archivos debemos crear un campo adicional
    documento_name = fields.Char(string='')
    valor_inmueble = fields.Float(string='Valor Comercial')
    imagenes_odoo = fields.Many2one(comodel_name='imagenes_binario', string='Imágenes')
    imagenesodoo_evidencia = fields.One2many(comodel_name='imagenes_binario', inverse_name='actas', string='')
    imagen_name = fields.Char()
    link = fields.Char()
    state = fields.Selection(string='', selection=[('nuevo', 'Nuevo'), ('activo', 'Activo'),('cerrado','Cerrado'),], 
    default='nuevo',
    copy=False
    )
    fecha_activa = fields.Datetime('Fecha Activado',copy=False)
    #funciones de botones
    def nuevo(self):
        self.state="nuevo"
    def activo(self):
        self.state="activo"
        self.fecha_activa=fields.Datetime.now()
    def cancelado(self):
        self.state="cerrado"
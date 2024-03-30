
from odoo import _, api, fields, models

from odoo.exceptions import UserError#esta libreria muestra errores en los registros

class actas(models.Model):
    _inherit =['image.mixin']# este es un modelo heredado para almacenar imágenes
    _name = 'actas_vecindad'
    _description = 'Actas de vecindad'
    name = fields.Char(string='Actas')
    usuario_id = fields.Many2one(comodel_name='res.partner', string='Usuario') #EL CMODEL ES EL LLAMADO DEL CAMPO
    #para filtra el modulo
    encargado_user = fields.Many2one(comodel_name='res.partner.category', string='Usuarios Encargado' , 
                                     #default=lambda self : self.env['res.partner.category'].search([('name','=','Sociales')])                                     
                                     default=lambda self : self.env.ref('actas_vecindad.categoria_sociales'))
    #asina valores por defecto , se usua funciones lambda
    fecha_acta = fields.Date(string='Fecha Acta')
    numero_obreros = fields.Integer(string='Numero Obreros')
    tipo_uso = fields.Many2one(comodel_name='tipo_uso', string='Tipo De Uso')
    encargado = fields.Many2many(comodel_name='encargado')
    calificacion = fields.Selection(string='Calificación', selection=[('alto', 'Alto'), ('medio', 'Medio'), ('bajo', 'Bajo'),])
    calificacion_alerta = fields.Char(string='Alert')

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
    fecha_cancelado = fields.Datetime('Fecha cancelado',copy=False)
    #funciones de botones
    def nuevo(self):
        self.state="nuevo"
        self.active=True
    def activo(self):
        self.state="activo"
        self.fecha_activa=fields.Datetime.now()
        self.active=True
#
    def cancelado(self):
        self.state="cerrado"
        self.fecha_cancelado=fields.Datetime.now()
        self.active=False

    def unlink(self):
        # if self.state =="cerrado":
        #     super(actas, self).unlink()
        #     #la funcion unlik es la funcion de odoo para eliminar datos en la db
        # else:
        #         raise UserError('no se puede eliminar si  NO esta en estado cancelado.')
        #     #equivale a un brake
        if self.state !="cerrado":
            raise UserError('no se puede eliminar si  NO esta en estado cancelado.')
            super(actas, self).unlink()
            #equivale a un brake
    # @api.onchange('calificacion')
    # def _onchange_calificacion(self):
    #     if self.calificacion:
    #         if self.calificacion =="alto":
    #             self.calificacion_alerta ='usuario colaborador'
    #         if self.calificacion =="medio":
    #             self.calificacion_alerta ='usuario de cuidado'
    #         if self.calificacion =="bajo":
    #             self.calificacion_alerta ='Alerta, usuario trafuga, alrta'
    #         else:
    #             self.calificacion_alerta= False



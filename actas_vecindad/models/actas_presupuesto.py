from odoo import _, api, fields, models

class ActasPresupuesto(models.Model):
    _name = 'actas.presupuesto'
    _description = 'Actas'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        string='Presupuesto', readonly=True )
    description = fields.Char(string='Descripcion')
    contacto_id = fields.Many2one(comodel_name='res.partner', string='Contacto', domain="[('is_company','=',False)]"
    )

    imagenes_actas = fields.Binary(
        string='imagenes_actas',
    )
    valor = fields.Float(string='valor')
    
    
    @api.model
    def create(self,variables):
        secuencia_actas_objeto = self.env['ir.sequence']
        secuencia_actas_variable = secuencia_actas_objeto.next_by_code('secuencia_presupuesto')
        variables['name'] = secuencia_actas_variable
        return super(ActasPresupuesto, self).create(variables)

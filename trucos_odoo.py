        
        # Trucos con los modelos
        if period:
            period_name = fields.Date.from_string(str(period.name))
            hasta_date = fields.Date.from_string(str(vals['date']))
            if period.do_not_settle and period_name >= hasta_date:
                raise UserError('No puede asentar un Asiento en una fecha que esta cerrada contablemente !!!')
        return super(AccountMove, self).create(vals)

        # PARAMETROS
        advance_payment = fields.Boolean(compute='_compute_giveme_advance_payment')

        @api.multi
        def _compute_giveme_advance_payment(self):
            adv_var = self.env['ir.config_parameter'].sudo().get_param('advance.payment')
            if adv_var == 'True':
                self.advance_payment  = True
            else:
                self.advance_payment = False

#  ONE2MANY OR 
Agregar [(4, line.product_id.supplier_taxes_id.id)] 


 
 Remplazar

 [(6,0,[line.product_id.supplier_taxes_id.id])]
For Many2many
For a many2many field, a list of tuples is expected. Here is the list of tuple that are accepted, with the corresponding semantics

(0, 0, { values }) link to a new record that needs to be created with the given values dictionary

(1, ID, { values }) update the linked record with id = ID (write values on it)

(2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

(3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)

(4, ID) link to existing record with id = ID (adds a relationship)

(5) unlink all (like using (3,ID) for all linked records)

(6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

Example: [(6, 0, [8, 5, 6, 4])] sets the many2many to ids [8, 5, 6, 4]

And One2many :
(0, 0, { values }) link to a new record that needs to be created with the given values dictionary

(1, ID, { values }) update the linked record with id = ID (write values on it)

(2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

Example: [(0, 0, {‘field_name’:field_value_record1, …}), (0, 0, {‘field_name’:field_value_record2, …})]

# ESTADOS

RO_STATES = {'draft': [('readonly', False)]}

class HrHourReport(models.Model):
    _name = 'hr.hour.report'
    _description = 'Hoja de Bonos RRHH'
    _inherit = ['mail.thread']
    _order = 'date_issue desc, name desc, id desc'
    
    line_ids = fields.One2many('hr.bonus.line', 'sheet_id', 'Bonos', readonly=True, states=RO_STATES)

#    FECHA ACTUAL
 date = fields.Date('Fecha contable', default=fields.Date.today)


#  CADENAS
cadena = cadena + u" Socio de Negocio: %s \n"%(socio_negocio)
cadena = notas + '\n' + u" NV: %s \n" % (nv)

# DELETE
alarm_ids = fields.Many2many('calendar.alarm', 'calendar_alarm_calendar_event_rel', string='Reminders', ondelete="restrict", copy=False)

EVITE BORRAR SI TIENE VALORES
alarm_ids = fields.Many2many('calendar.alarm', 'calendar_alarm_calendar_event_rel', string='Reminders', ondelete="restrict", copy=False)

CASCADE: Delete the Course record with matching student_id when Student is deleted

RESTRICT: Cannot delete the Student as long as it is related to a Course.

NO ACTION: similar, but is a deferred check: You can delete the Student but you have to make sure that the integrity is OK when the transaction is committed.

SET DEFAULT: uses openerp default definition (see _defaults dict in the python model definition)

SET NULL: when a Student gets deleted, the student_id becomes NULL in the DB.


# COLOCANDO SECUENCIA A UNA VISTA TREE
sequence = fields.Integer(compute='_compute_sequence')

    @api.multi
    def _compute_sequence(self):
        for i, record in enumerate(self.sorted('id', reverse=True), 1):
            record.sequence = i

# PARAMETROS
limit_day = self.env['ir.config_parameter'].sudo().get_param('cancel.sale.order')

# UTILIZACION DE MAPPEED
stock = sum(locations.with_context({'template_id': record.id}).mapped('virtual_available'))

# IMPORTAR CORRECTAMENTE UNA LIBRERIA PY
try:
	import barcode
	from barcode.writer import ImageWriter
except ImportError as exc:
	_logger.error('Faltan dependencias: %s', exc)


# TRABAJOS CON FECHAS
from datetime import datetime, timedelta

@api.one
    @api.depends('desde_date', 'hasta_date')
    def _calcular_si_es_mes(self):
        hoy = datetime.now().date()
        desde = self.desde_date
        fecha_desde = datetime.strptime(str(desde), '%Y-%m-%d')
        if str(fecha_desde) < str(hoy):
            if self.hasta_date:
                hasta_date = datetime.strptime(str(self.hasta_date), '%Y-%m-%d')
                if str(hasta_date) > str(hoy):
                    self.del_mes = True
            else:
                self.del_mes = True
        else:
            self.del_mes = False

        # CAMPOS TIPO MONEDA

        amount_total = fields.Monetary('Total')

# RAISE
from odoo.exceptions import UserError

raise UserError(_('%s no tiene contrato para el periodo %s - %s') % (employee.display_name, date_from, date_to))

raise UserError(_('El monto por préstamos no coincide:\nCuotas por pagar: %f\nMonto préstamo en nómina: %s') % (round(total_cuotas), round(total_prestamos)))

# LOG EN CAMPOS DE ESTADOS
state = fields.Selection([('pending', 'Pendiente'), ('error', 'Errores')], 'Estado', required=True, track_visibility='onchange')

# CREAR COMO ADMIN
insert = self.env['tag.list'].sudo().create(vals)


# FECHA ACTUAL
from datetime import datetime
a = datetime.today()

# REDEFINIENDO METODOS
 @api.multi
    def button_mark_done(self):
        if not self.tag_mrp_ids:
            raise ValidationError(_("Importante! Por favor defina los tags"))
        res = super(MrpProduction, self).do_transfer()
        return res


# <?xml version="1.0"?>
<odoo>
   <data noupdate="0">
   	<record id="login_form_disable_footer" model="ir.config_parameter">
           <field name="key">login_form_disable_footer</field>
           <field name="value">False</field>
       </record>
   </data>
</odoo>

cr = request.cr
uid = odoo.SUPERUSER_ID
param_obj = request.env['ir.config_parameter']

change_background = ast.literal_eval(param_obj.get_param('login_form_change_background_by_hour')) or False
config_login_timezone = param_obj.get_param('login_form_change_background_timezone')

# ERROR
from odoo.exceptions import ValidationError
raise ValidationError(_("Importante! Por favor defina los tags"))

# HERENCIA EN EL MODELO
class SaleOrderNotCopy(models.Model):
    _inherit = "sale.order"
    user_id = fields.Many2one('res.users', copy=False)

# OBTENER DATOS DESDE LA COMPAÑIA
self.env.user.company_id.name

# STOCK DE UN PRODUCTO
stock = sum(id.stock_quant_ids.mapped('qty'))

# TIPOD DE CAMPOS EN ODOO
folio = fields.Integer(string='Folio:', size=10)
name = fields.Char(string='New Value', size=64, required=True)
online_mode = fields.Boolean('Online Mode', help='Si esta activo', default='True')

doc_type = fields.Selection(
            [('D','RUT Chile'),
            ('P','Pasaportes'),
            ('C ','Permiso de conducir Chile '),
            ('I','Carta o documento de identidad'),
            ('X','Permiso de residencia UE'),
            ('N','Permiso de residencia Chile ')],
            'Tipo de Documento', size=1)
            
gender = fields.Selection([('F','Femenino'),('M','Masculino')],'Sexo',size=1)
  
company_id = fields.Many2one('res.company', string='Compañía', change_default=True, readonly=True,
            default=lambda self: self.env['res.company']._company_default_get('traveler.register'))
            
entry_date = fields.Datetime('Fecha de Entrada', default = lambda self: datetime.today())

# COLOCANDO VALORES POR DEFECTO
@api.model
    def create(self, vals):
        vals['property_payment_term_id'] = 1
        return super(res_partner_cnp, self).create(vals)

        # SALTO DE LINEA
        'comment': note and note_sale+'\n'+note or note_sale

    #   CADENAS
     cadena = u" Dir. Intermediaria: %s, %s \n Dir. Final: %s, %s "%(direccion_1,ciudad,direccion_2,ciudad2)
      
    #   REDONDEAR CON DECIMALES
 monto = fields.Float('Monto', digits=(10, 4))

#  OPCIONES EN LOS CAMPOS BASICOS EN ODOO
from openerp import models, fields

class AModel(models.Model):

    _name = 'a_name'

    name = fields.Char(
        string="Name",                   # Optional label of the field
        compute="_compute_name_custom",  # Transform the fields in computed fields
        store=True,                      # If computed it will store the result
        select=True,                     # Force index on field
        readonly=True,                   # Field will be readonly in views
        inverse="_write_name"            # On update trigger
        required=True,                   # Mandatory field
        translate=True,                  # Translation enable
        help='blabla',                   # Help tooltip text
        company_dependent=True,          # Transform columns to ir.property
        search='_search_function'        # Custom search function mainly used with compute
    )

    # FUNCION ONCHANGE
        partner_id = fields.Many2one('res.partner','Socio')
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        partner_id = self.partner_id
        if partner_id:
            self.first_name = partner_id.name
            if not partner_id.country_id:
                raise UserError(_('Error 0001: No existe el pais'))
            self.birth_country = partner_id.country_id.id

    # CALCULANDO COMISION EN LA FACTURA
    total = 0
for line in self.invoice_line_ids:
    if line.product_id:
        total += (line.product_id.sale_commission or 0.0) / 100.0 * line.price_unit * line.quantity
self.sale_commission = total


# CLASE INICIAL MODELO HERENCIA

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from datetime import datetime

class LibreDTEResCompany(models.Model):
    _inherit = "res.company"
    libredte_hash = fields.Char('LibreDTE hash', help="Code from LibreDTE")
    dte_preliminar = fields.Boolean('DTE Preliminar', help='Si')
    online_mode = fields.Boolean('Online Mode', help='Si', default='True')


# CLASE INICIAL MODELO HERENCIA
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record model="ir.ui.view" id="webfactura_view_company_inherit_form">
        <field name="name">webfactura.view.company.inherit.form</field>
        <field name="inherit_id" ref="base.view_company_form"/>
        <field name="model">res.company</field>
        <field name="arch" type="xml">
            <notebook>
                <page string="LibreDTE">
                    <group cols="4">
                        <field name="libredte_hash" password="True" class="oe_inline" required="1"/>
                        <field name="dte_preliminar" />
                        <field name="online_mode" />
                    </group>
                </page>
            </notebook>
        </field>
    </record>
</odoo>

# HERENCIA DE CAMPO
<?xml version="1.0" encoding="UTF-8"?>
 <odoo>
    <data>
        <record model="ir.ui.view" id="partner_instructor_form_view">
            <field name="name">partner.instructor</field>
            <field name="model">res.partner</field>
            <field name="inherit_id" ref="base.view_partner_form"/>
            <field name="arch" type="xml"> 
               <field name="category_id" position="after" >          
                    <field name="rut" string="RUC:" placeholder="00000000" />
                    <field name="mail" string="Correo"/> 
               </field>                       
            </field>
        </record>
    </data>
</odoo>


# CLASE INICIAL MODELO
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class rrhh_afp(models.Model):
    _description = "AFP Fondo de Pension"
    _name = 'rrhh.afp'

    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Name', translate=True)
    rut = fields.Char('Rut', translate=True)
    tasa = fields.Float('Tasa', required=True)
    sis = fields.Float('Aporte Empresa', required=True)
    independiente = fields.Float('Independientes', required=True)

    # CLASE INICIAL VISTA
    <?xml version="1.0" encoding="UTF-8"?>
 <odoo>
    <data>

    <record id="view_form_rrhh_afp" model="ir.ui.view">
             <field name="name">view.form.rrhh.afp</field>
             <field name="model">rrhh.afp</field>
             <field name="arch" type="xml">
                <form string="Listado de AFP">
                  <sheet>
                    <legend>AFP</legend>
                       <group>
                          <group>
                             <field name="rut"/>
                             <field name="name"/>
                             <field name="codigo"/>
                             <field name="tasa"/>
                             <field name="sis"/>
                             <field name="independiente"/>
                          </group>
                       </group>




# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaMedicinaHistoria(models.Model) :
    _name = 'medicina.cita.medicina.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Medicina General'
    
    medicina_abdomen = fields.Selection(string='''Abdomen''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_abdomen_razon = fields.Text(string='''Razón''')
    medicina_abeg = fields.Boolean(string='''ABEG''')
    medicina_abeh = fields.Boolean(string='''ABEH''')
    medicina_aben = fields.Boolean(string='''ABEN''')
    medicina_anamnesis = fields.Text(string='''Anamnesis''')
    medicina_anillos_inguinales = fields.Selection(string='''Anillos Inguinales''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_anillos_inguinales_razon = fields.Text(string='''Razón''')
    medicina_anormalidades_regional = fields.Char(string='''Anormalidades''')
    medicina_ap_locomotor = fields.Selection(string='''Ap. Locomotor''',selection=[("conservado","Conservado"),("disminuido","Disminuido")])
    medicina_ap_locomotor_razon = fields.Char(string='''Razón''')
    medicina_boca = fields.Selection(string='''Boca''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_boca_razon = fields.Text(string='''Razón''')
    medicina_cabeza_cabello = fields.Selection(string='''Cabeza y Cabello''',selection=[("normal","Normal"),("anormal","Anormal")])
    medicina_cabeza_cabello_razon = fields.Text(string='''Razón''')
    medicina_columna = fields.Selection(string='''Columna''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_columna_razon = fields.Text(string='''Razón''')
    medicina_corazon = fields.Selection(string='''Corazón''',selection=[("normal","Normal"),("anormal","Anormal")])
    medicina_corazon_razon = fields.Char(string='''Razón''')
    medicina_cuello_garganta = fields.Selection(string='''Cuello y Garganta''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_cuello_garganta_razon = fields.Text(string='''Razón''')
    medicina_ectoscopia = fields.Selection(string='''Ectoscopía''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_ectoscopia_razon = fields.Char(string='''Razón''')
    medicina_faringe = fields.Selection(string='''Faringe''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_faringe_razon = fields.Text(string='''Razón''')
    medicina_genitales = fields.Selection(string='''Genitales''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_genitales_razon = fields.Text(string='''Razón''')
    medicina_genito_urinario = fields.Selection(string='''Genito-Urinario''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_genito_urinario_razon = fields.Text(string='''Razón''')
    medicina_hernias = fields.Boolean(string='''Hernias''')
    medicina_hernias_razon = fields.Text(string='''Razón''')
    medicina_lotep = fields.Boolean(string='''LOTEP''')
    medicina_mama_derecha = fields.Selection(string='''Mama Derecha''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_mama_derecha_razon = fields.Char(string='''Razón''')
    medicina_mama_izquierda = fields.Selection(string='''Mama Izquierda''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_mama_izquierda_razon = fields.Char(string='''Razón''')
    medicina_marcha_tandem = fields.Selection(string='''Marcha Tandem''',selection=[("conservado","Conservado"),("anormal","Anormal"),("no_realizado","No Realizado")])
    medicina_marcha_tandem_razon = fields.Char(string='''Razón''')
    medicina_miembro_inferior_derecho = fields.Selection(string='''Miembro Inferior Derecho''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_inferior_derecho_razon = fields.Char(string='''Razón''')
    medicina_miembro_inferior_izquierdo = fields.Selection(string='''Miembro Inferior Izquierdo''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_inferior_izquierdo_razon = fields.Char(string='''Razón''')
    medicina_miembro_superior_derecho = fields.Selection(string='''Miembro Superior Derecho''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_superior_derecho_razon = fields.Char(string='''Razón''')
    medicina_miembro_superior_izquierdo = fields.Selection(string='''Miembro Superior Izquierdo''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_superior_izquierdo_razon = fields.Char(string='''Razón''')
    medicina_nariz = fields.Selection(string='''Nariz''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_nariz_razon = fields.Text(string='''Razón''')
    medicina_piel_faneras = fields.Selection(string='''Piel y Faneras''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_piel_faneras_razon = fields.Text(string='''Razón''')
    medicina_pulmones = fields.Selection(string='''Pulmones''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_pulmones_razon = fields.Char(string='''Razón''')
    medicina_sistema_linfatico = fields.Selection(string='''Sistema Linfático''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_sistema_linfatico_razon = fields.Text(string='''Razón''')
    medicina_sistema_nervioso = fields.Selection(string='''Sistema Nervioso''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_sistema_nervioso_razon = fields.Text(string='''Razón''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.medicina.historia''', relation='''medicina_cita_medicina_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaMedicina(models.Model) :
    _name = 'medicina.cita.medicina'
    _description = 'Cita de Medicina General'
    _inherits = {'medicina.cita.medicina.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.medicina.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.medicina''', relation='''medicina_cita_medicina_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

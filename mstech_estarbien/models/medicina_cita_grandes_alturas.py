# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaGrandesAlturasHistoria(models.Model) :
    _name = 'medicina.cita.grandes_alturas.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Grandes Alturas'
    
    grandes_alturas_alergias = fields.Boolean(string='''Alergias''')
    grandes_alturas_alergias_descripcion = fields.Char(string='''Alergias (descripción)''')
    grandes_alturas_apnea_sueno = fields.Boolean(string='''Apnea del sueño''')
    grandes_alturas_aptitud_trabajo = fields.Selection(string='''Aptitud para trabajo en grandes alturas''',selection=[("apto","Apto"),("apto_con_restriccion","Apto con restricción"),("no_apto","No apto")])
    grandes_alturas_cirugia_mayor_reciente = fields.Boolean(string='''Cirugía mayor reciente''')
    grandes_alturas_desordenes_coagulacion = fields.Boolean(string='''Desórdenes de la coagulación: trombosis, otros''')
    grandes_alturas_diabetes_mellitus = fields.Boolean(string='''Diabetes mellitus''')
    grandes_alturas_embarazo = fields.Boolean(string='''Embarazo''')
    grandes_alturas_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (grandes alturas)''')
    grandes_alturas_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria (grandes alturas)''')
    grandes_alturas_hipertension_arterial = fields.Boolean(string='''Hipertensión arterial''')
    grandes_alturas_indice_masa_corporal = fields.Float(string='''Índice de masa corporal (grandes alturas)''')
    grandes_alturas_infecciones_recientes = fields.Boolean(string='''Infecciones recientes (de moderadas a severas)''')
    grandes_alturas_medicacion_actual = fields.Boolean(string='''Uso de medicación actual''')
    grandes_alturas_medicacion_actual_descripcion = fields.Text(string='''Uso de medicación actual (descripción)''')
    grandes_alturas_obesidad = fields.Boolean(string='''Obesidad''')
    grandes_alturas_observaciones = fields.Text(string='''Observaciones (grandes alturas)''')
    grandes_alturas_otra_contraindicacion = fields.Boolean(string='''Otra contraindicación médica importante''')
    grandes_alturas_otra_contraindicacion_descripcion = fields.Char(string='''Otra contraindicación médica importante (descripción)''')
    grandes_alturas_presion_arterial = fields.Char(string='''Presión arterial (grandes alturas)''')
    grandes_alturas_problemas_cardiacos = fields.Boolean(string='''Problemas cardiacos: marcapasos, coronariopatía, otros''')
    grandes_alturas_problemas_digestivos = fields.Boolean(string='''Problemas digestivos: sangrado digestivo, hepatitis, cirrosis hepática, otros''')
    grandes_alturas_problemas_neurologicos = fields.Boolean(string='''Problemas neurológicos: epilepsia, vértigos, otros''')
    grandes_alturas_problemas_oftalmologicos = fields.Boolean(string='''Problemas oftalmológicos: retinopatía, glaucoma, otros''')
    grandes_alturas_problemas_respiratorios = fields.Boolean(string='''Problemas respiratorios: asma, EPOC, otros''')
    grandes_alturas_saturacion_oxigeno = fields.Float(string='''Saturación de oxígeno (grandes alturas)''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.grandes_alturas.historia''', relation='''medicina_cita_grandes_alturas_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaGrandesAlturas(models.Model) :
    _name = 'medicina.cita.grandes_alturas'
    _description = 'Cita de Grandes Alturas'
    _inherits = {'medicina.cita.grandes_alturas.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.grandes_alturas.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.grandes_alturas''', relation='''medicina_cita_grandes_alturas_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

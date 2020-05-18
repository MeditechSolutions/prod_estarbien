# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaElectrocardiogramaHistoria(models.Model) :
    _name = 'medicina.cita.electrocardiograma.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de EKG'
    
    ekg_antecedentes_familiares = fields.Char(string='''Antecedentes familiares''')
    ekg_aptitud_trabajo_altura = fields.Selection(string='''Aptitud para trabajos en altura mayor a 2500m''',selection=[("apto","Apto"),("no_apto","No apto")])
    ekg_aptitud_trabajo_forzado = fields.Selection(string='''Aptitud para trabajo forzado''',selection=[("apto","Apto"),("no_apto","No apto")])
    ekg_asintomatico = fields.Boolean(string='''Asintomático''')
    ekg_cansancio_rapido = fields.Boolean(string='''Cansancio rápido''')
    ekg_choque_punta = fields.Char(string='''Choque de la punta (interpretación EKG)''')
    ekg_claudicacion_intermitente = fields.Boolean(string='''Claudicación intermitente''')
    ekg_diabetes = fields.Boolean(string='''Diabetes''')
    ekg_diagnostico = fields.Selection(string='''Diagnóstico (electrocardiograma)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    ekg_dinitrofenol = fields.Boolean(string='''Dinitrofenol''')
    ekg_dislipidemias = fields.Boolean(string='''Dislipidemias''')
    ekg_dolor_precordial_antecedentes = fields.Boolean(string='''Dolor precordial''')
    ekg_dolor_precordial_sintomas_actuales = fields.Boolean(string='''Dolor precordial (síntomas actuales)''')
    ekg_eje_qrs = fields.Float(string='''Eje QRS (interpretación EKG)''')
    ekg_examen_corazon = fields.Char(string='''Examen del corazón''')
    ekg_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (interpretación EKG)''')
    ekg_frecuencia_cardiaca_preferencial = fields.Integer(string='''Frecuencia cardiaca preferencial''')
    ekg_infarto_agudo_miocardio = fields.Boolean(string='''IMAs''')
    ekg_intervalo_pr = fields.Float(string='''Intervalo PR (interpretación EKG)''')
    ekg_intervalo_qrs = fields.Float(string='''Intervalo QRS (interpretación EKG)''')
    ekg_intervalo_qt = fields.Float(string='''Intervalo QT (interpretación EKG)''')
    ekg_lipotimias = fields.Boolean(string='''Lipotimias''')
    ekg_mareos = fields.Boolean(string='''Mareos''')
    ekg_mareos_sintomas_actuales = fields.Boolean(string='''Mareos (síntomas actuales)''')
    ekg_obesidad = fields.Boolean(string='''Obesidad''')
    ekg_onda_p = fields.Float(string='''Onda P (interpretación EKG)''')
    ekg_onda_q = fields.Float(string='''Onda Q (interpretación EKG)''')
    ekg_onda_r = fields.Float(string='''Onda R (interpretación EKG)''')
    ekg_onda_s = fields.Float(string='''Onda S (interpretación EKG)''')
    ekg_onda_t = fields.Float(string='''Onda T (interpretación EKG)''')
    ekg_onda_u = fields.Float(string='''Onda U (interpretación EKG)''')
    ekg_otros_antecedentes_cardiologicos = fields.Char(string='''Otros antecedentes cardiológicos''')
    ekg_otros_hallazgos_corazon = fields.Char(string='''Otros hallazgos en el corazón''')
    ekg_otros_sintomas_cardiologicos = fields.Char(string='''Otros síntomas cardiológicos''')
    ekg_palpitaciones = fields.Boolean(string='''Palpitaciones''')
    ekg_palpitaciones_sintomas_actuales = fields.Boolean(string='''Palpitaciones (síntomas actuales)''')
    ekg_perdida_de_conciencia = fields.Boolean(string='''Pérdida de conciencia''')
    ekg_presion_alta = fields.Boolean(string='''Presión alta''')
    ekg_presion_arterial = fields.Char(string='''Presión arterial (interpretación EKG)''')
    ekg_presion_arterial_preferencial = fields.Char(string='''Presión arterial preferencial''')
    ekg_ritmo = fields.Char(string='''Ritmo (interpretación EKG)''')
    ekg_segmento_st = fields.Float(string='''Segmento ST (interpretación EKG)''')
    ekg_soplo_cardiaco = fields.Boolean(string='''Soplo cardiaco''')
    ekg_tabaquismo = fields.Boolean(string='''Tabaquismo''')
    ekg_varices_miembros_inferiores = fields.Boolean(string='''Várices en miembros inferiores''')
    archivo_adjunto_cardiologico = fields.Binary(string='''Archivo''')
    archivo_adjunto_cardiologico_filename = fields.Char(string='''Filename for archivo_adjunto_informe_cardiologico''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.electrocardiograma.historia''', relation='''medicina_cita_electrocardiograma_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaElectrocardiograma(models.Model) :
    _name = 'medicina.cita.electrocardiograma'
    _description = 'Cita de EKG'
    _inherits = {'medicina.cita.electrocardiograma.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.electrocardiograma.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.electrocardiograma''', relation='''medicina_cita_electrocardiograma_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

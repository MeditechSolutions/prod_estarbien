# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaPsicologiaHistoria(models.Model) :
    _name = 'medicina.cita.psicologia.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Psicología'
    
    psicologico_afectividad_observaciones = fields.Char(string='''Afectividad (informe psicológico)''')
    psicologico_afectividad_rasgos = fields.Char(string='''Afectividad (rasgos)''')
    psicologico_afectividad_sin_datos_relevantes = fields.Char(string='''Afectividad (sin datos relevantes)''')
    psicologico_afectividad_transtorno = fields.Char(string='''Afectividad (transtorno)''')
    psicologico_area_personalidad_rasgos = fields.Char(string='''Área de la personalidad (rasgos)''')
    psicologico_area_personalidad_sin_datos_relevantes = fields.Char(string='''Área de la personalidad (sin datos relevantes)''')
    psicologico_area_personalidad_transtorno = fields.Char(string='''Área de la personalidad (transtorno)''')
    psicologico_bateria_conductores = fields.Boolean(string='''Batería de conductores''')
    psicologico_bateria_dna_luria = fields.Boolean(string='''Batería DNA de Luria (diagnóstico neuropsicológico de adultos)''')
    psicologico_clima_laboral = fields.Boolean(string='''Clima laboral (técnica psicológica)''')
    psicologico_conclusiones = fields.Char(string='''Conclusiones (informe psicológico)''')
    psicologico_conducta_discurso_articulacion = fields.Selection(string='''Articulacion del discurso (informe psicológico)''',selection=[("con_dificultad","Con dificultad"),("sin_dificultad","Sin dificultad")])
    psicologico_conducta_discurso_ritmo = fields.Selection(string='''Ritmo del discurso (informe psicológico)''',selection=[("lento","Lento"),("rapido","Rápido"),("fluido","Fluído")])
    psicologico_conducta_discurso_tono = fields.Selection(string='''Tono del discurso (informe psicológico)''',selection=[("bajo","Bajo"),("moderado","Moderado"),("alto","Alto")])
    psicologico_conducta_orientacion_espacio = fields.Selection(string='''Orientación en el espacio (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_orientacion_persona = fields.Selection(string='''Orientación en la persona (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_orientacion_tiempo = fields.Selection(string='''Orientación en el tiempo (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_postura = fields.Selection(string='''Postura (informe psicológico)''',selection=[("erguida","Erguida"),("encorvada","Encorvada")])
    psicologico_conducta_presentacion = fields.Selection(string='''Presentación (informe psicológico)''',selection=[("adecuado","Adecuado"),("inadecuado","Inadecuado")])
    psicologico_coordinacion_observaciones = fields.Char(string='''Coordinación visomotriz (informe psicológico)''')
    psicologico_diagnostico = fields.Selection(string='''Tipo de diagnóstico (informe psicológico)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    psicologico_emocional = fields.Text(string='''Resultado emocional (informe psicológico)''')
    psicologico_entrevista = fields.Boolean(string='''Entrevista (técnica psicológica)''')
    psicologico_escala_apreciacion_estres = fields.Boolean(string='''Escala de apreciación del estrés (EAE)''')
    psicologico_escala_memoria_wechsler = fields.Boolean(string='''Escala de memoria de Wechsler''')
    psicologico_estres_observaciones = fields.Char(string='''Estrés (informe psicológico)''')
    psicologico_fatiga_laboral = fields.Selection(string='''Fatiga laboral (informe psicológico)''',selection=[("no_presenta","No presenta"),("presenta","Presenta")])
    psicologico_fobia_observaciones = fields.Char(string='''Fobia (informe psicológico)''')
    psicologico_inventario_ansiedad_zung = fields.Boolean(string='''Inventario de ansiedad Zung''')
    psicologico_inventario_depresion_zung = fields.Boolean(string='''Inventario de depresión Zung''')
    psicologico_mbi = fields.Boolean(string='''Inventario de "Burnout" de Maslach (MBI)''')
    psicologico_mips = fields.Boolean(string='''Inventario Millon de estilos de Personalidad (MIPS)''')
    psicologico_motivaciones_psicosociales = fields.Boolean(string='''Escala de motivaciones psicosociales (MPS)''')
    psicologico_motivo_evaluacion = fields.Char(string='''Motivo de la evaluación (informe psicológico)''')
    psicologico_nivel_intelectual_observaciones = fields.Char(string='''Nivel intelectual (informe psicológico)''')
    psicologico_nivel_memoria_observaciones = fields.Char(string='''Nivel de memoria (informe psicológico)''')
    psicologico_observacion = fields.Boolean(string='''Observación (técnica psicológica)''')
    psicologico_otras_tecnicas_instrumentos = fields.Char(string='''Otras técnicas o instrumentos utilizados (informe psicológico)''')
    psicologico_recomendaciones = fields.Text(string='''Recomendaciones (informe psicológico)''')
    psicologico_resultado_diagnostico = fields.Selection(string='''Resultado del diagnóstico (informe psicológico)''',selection=[("apto","Apto"),("apto_con_observaciones","Apto con observaciones"),("no_apto","No apto"),("apto_con_restricciones","Apto con restricciones")])
    psicologico_somnolencia_diurna = fields.Selection(string='''Somnolencia diurna (informe psicológico)''',selection=[("no_presenta","No presenta"),("presenta_alta_probabilidad","Presenta alta probabilidad")])
    psicologico_test_bender = fields.Boolean(string='''Test de Bender''')
    psicologico_test_benton = fields.Boolean(string='''Test de Benton''')
    psicologico_wais = fields.Boolean(string='''Escala Wechsler de Inteligencia para Adultos (WAIS)''')
    archivo_adjunto_psicologico_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_psicologico_1_filename = fields.Char(string='''Filename for archivo_adjunto_psicologia_1''')
    archivo_adjunto_psicologico_2 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_psicologico_2_filename = fields.Char(string='''Filename for archivo_adjunto_psicologia_2''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.psicologia.historia''', relation='''medicina_cita_psicologia_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaPsicologia(models.Model) :
    _name = 'medicina.cita.psicologia'
    _description = 'Cita de Psicología'
    _inherits = {'medicina.cita.psicologia.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.psicologia.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.psicologia''', relation='''medicina_cita_psicologia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaEspirometria(models.Model) :
    _name = 'medicina.cita.espirometria'
    _inherit = 'medicina.cita'
    _description = 'Cita de Espirometría'
    
    espirometria_informe_medico = fields.Text(string='''Informe médico''')
    espirometria_diagnostico = fields.Selection(string='''Diagnóstico (espirometría)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    espirometria_informe_medico_recomendaciones = fields.Text(string='''Recomendaciones de informe médico (espirometría)''')
    espirometria_fvc_teor = fields.Char(string='''Capacidad vital forzada (teórica) (FVC)''')
    espirometria_fev1_teor = fields.Char(string='''Volumen espiratorio forzado en el primer segundo (teórico) (FEV1)''')
    espirometria_fev1_fvc_teor = fields.Char(string='''Cociente FEV1/FVC (teórico)''')
    espirometria_pef_teor = fields.Char(string='''Flujo espiratorio máximo (teórico) (PEF)''')
    espirometria_fef2575_teor = fields.Char(string='''Flujo espiratorio medio (teórico) (FEF 25-75%)''')
    espirometria_fvc_pre = fields.Char(string='''Capacidad vital forzada (pre) (FVC''')
    espirometria_fev1_pre = fields.Char(string='''Volumen espiratorio forzado en el primer segundo (pre) (FEV1)''')
    espirometria_fev1_fvc_pre = fields.Char(string='''Cociente FEV1/FVC (pre)''')
    espirometria_pef_pre = fields.Char(string='''Flujo espiratorio máximo (pre) (PEF)''')
    espirometria_fef2575_pre = fields.Char(string='''Flujo espiratorio medio (pre) (FEF 25-75%)''')
    espirometria_conclusion = fields.Selection(string='''Conclusión (espirometría)''',selection=[("patron_normal_espirometrico","Patrón normal espirométrico"),("con_alteracion_funcional","Con alteración funcional")])
    espirometria_conclusion_razon = fields.Text(string='''Razón de la conclusión''')
    espirometria_desprendimiento_retina_cirugia = fields.Boolean(string='''¿Tuvo algún desprendimiento de retina o una operación (cirugía) de los ojos, tórax o abdomen en los últimos 3 meses?''')
    espirometria_ataque_cardiaco_infarto = fields.Boolean(string='''¿Ha tenido algún ataque al cardíaco o infarto al corazón en los últimos 3 meses?''')
    espirometria_hospitalizado_problemas_corazon = fields.Boolean(string='''¿Ha estado hospitalizado(a) por cualquier otro problema del corazón en los últimos 3 meses?''')
    espirometria_medicamentos_tuberculosis = fields.Boolean(string='''¿Está usando medicamentos para la tuberculosis, en este momento?''')
    espirometria_embarazo = fields.Boolean(string='''¿Está usted embarazada actualmente?''')
    espirometria_hemoptisis = fields.Boolean(string='''Hemoptisis''')
    espirometria_neumotorax = fields.Boolean(string='''Neumotórax''')
    espirometria_traqueostomia = fields.Boolean(string='''Traqueostomía''')
    espirometria_sonda_pleural = fields.Boolean(string='''Sonda pleural''')
    espirometria_aneurisma = fields.Boolean(string='''Aneurisma (cerebral, abdominal o tórax)''')
    espirometria_embolia_pulmonar = fields.Boolean(string='''Embolia pulmonar''')
    espirometria_infarto_reciente = fields.Boolean(string='''Infarto reciente''')
    espirometria_inestabilidad_cardiovascular = fields.Boolean(string='''Inestabilidad cardiovascular''')
    espirometria_fiebre_nausea_vomito = fields.Boolean(string='''Fiebre, náuseas y/o vómito''')
    espirometria_embarazo_avanzado = fields.Boolean(string='''Embarazo avanzado''')
    espirometria_embarazo_complicado = fields.Boolean(string='''Embarazo complicado''')
    espirometria_infeccion_respiratoria_3_semanas = fields.Boolean(string='''¿Tuvo una infección respiratoria (resfriado) en las últimas 3 semanas?''')
    espirometria_infeccion_oido_3_semanas = fields.Boolean(string='''¿Tuvo una infección en el oído en las últimas 3 semanas?''')
    espirometria_aerosoles_nebulizaciones_3_horas = fields.Boolean(string='''¿Uso aerosoles (sprays inhalados) o nebulizaciones con broncodilatadores, en las últimas 3 horas?''')
    espirometria_brondocilatador_8_horas = fields.Boolean(string='''¿Ha usado algún medicamento broncodilatador en las últimas 8 horas?''')
    espirometria_fuma_2_horas = fields.Boolean(string='''¿Fumó (cualquier tipo de cigarro) en las últimas dos horas?''')
    espirometria_fuma_2_horas_descripcion = fields.Char(string='''¿Cuántos cigarros fumó (cualquier tipo de cigarro) en las últimas dos horas?''')
    espirometria_ejercicio_fisico_ultima_hora = fields.Boolean(string='''¿Realizó algún ejercicio físico fuerte (gimnasia, caminata, trote) en la última hora?''')
    espirometria_comida_ultima_hora = fields.Boolean(string='''¿Comió en la úlltima hora?''')
    archivo_adjunto_espirometrico_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_espirometrico_1_filename = fields.Char(string='''Filename for archivo_adjunto_espirometrico_1''')
    archivo_adjunto_espirometrico_2 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_espirometrico_2_filename = fields.Char(string='''Filename for archivo_adjunto_espirometrico_2''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.espirometria''', relation='''medicina_cita_espirometria_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

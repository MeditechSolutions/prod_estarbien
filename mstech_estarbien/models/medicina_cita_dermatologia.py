# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaDermatologiaHistoria(models.Model) :
    _name = 'medicina.cita.dermatologia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Dermatología'
    
    dermatologia_cambio_coloracion_cuestionario = fields.Boolean(string='''¿Presenta algún cambio de coloración en la piel?''')
    dermatologia_cambios_unas_cuestionario = fields.Boolean(string='''¿Presenta cambios en las uñas?''')
    dermatologia_comentarios_cuestionario = fields.Text(string='''Comentarios (cuestionario de dermatología)''')
    dermatologia_comezon_cuestionario = fields.Boolean(string='''¿Tiene comezón?''')
    dermatologia_comezon_localizacion = fields.Char(string='''¿Dónde se localiza la comezón?''')
    dermatologia_dermatopatia_medico = fields.Boolean(string='''Al examen físico, ¿presenta el paciente alguna lesión sugerente a dermatopatía?''')
    dermatologia_enfermedades_piel_cuestionario = fields.Boolean(string='''¿Sufre Ud. enfermedades de la piel?''')
    dermatologia_enfermedades_piel_diagnostico = fields.Char(string='''¿Qué diagnóstico le han dado de dichas enfermedades?''')
    dermatologia_enrojecimiento_cuestionario = fields.Boolean(string='''¿Ud. tiene enrojecimiento de alguna zona del cuerpo?''')
    dermatologia_enrojecimiento_localizacion = fields.Char(string='''¿Dónde se localiza el enrojecimiento?''')
    dermatologia_equipo_proteccion_personal_cuestionario = fields.Boolean(string='''¿Usa EPP (equipo de protección personal)?''')
    dermatologia_equipo_proteccion_personal_especifico = fields.Char(string='''¿Qué tipo de EPP usa?''')
    dermatologia_fotoprotector_recomendado = fields.Char(string='''Fotoprotector recomendado''')
    dermatologia_fototipo_piel = fields.Selection(string='''Tipo de fototipo de piel''',selection=[("fototipo_i","Fototipo I"),("fototipo_ii","Fototipo II"),("fototipo_iii","Fototipo III"),("fototipo_iv","Fototipo IV"),("fototipo_v","Fototipo V"),("fototipo_vi","Fototipo VI")])
    dermatologia_hinchazon_cuestionario = fields.Boolean(string='''¿Presenta hinchazón en parte de su cuerpo?''')
    dermatologia_hinchazon_localizacion = fields.Char(string='''¿Dónde se localiza la hinchazón?''')
    dermatologia_interconsulta_medico = fields.Boolean(string='''¿Necesita el paciente interconsulta con la especialidad de dermatología?''')
    dermatologia_lesion_cuestionario = fields.Boolean(string='''¿Tiene alguna lesión?''')
    dermatologia_lesion_duracion = fields.Char(string='''¿Desde cuándo tiene la lesión?''')
    dermatologia_lesion_frecuente_cuestionario = fields.Boolean(string='''¿Estas lesiones se repiten varias veces al año?''')
    dermatologia_lesion_localizacion = fields.Char(string='''¿Dónde se localiza la lesión?''')
    dermatologia_mas_pruebas_medico = fields.Boolean(string='''El paciente necesita ser evaluado por médico dermatologico para la realización de las siguientes pruebas : Pruebas de sensibilidad subcotánea, Luz de Wood y Maniobra de Nikolsky''')
    dermatologia_medicacion_cuestionario = fields.Boolean(string='''¿Está tomando alguna medicación?''')
    dermatologia_rinitis_asma_cuestionario = fields.Boolean(string='''¿Sufre de rinitis alérgica o asma?''')
    dermatologia_tamizaje_observaciones = fields.Text(string='''Observaciones de tamizaje (dermatología)''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.dermatologia.historia''', relation='''medicina_cita_dermatologia_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaDermatologia(models.Model) :
    _name = 'medicina.cita.dermatologia'
    _description = 'Cita de Dermatología'
    _inherits = {'medicina.cita.dermatologia.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.dermatologia.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.dermatologia''', relation='''medicina_cita_dermatologia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

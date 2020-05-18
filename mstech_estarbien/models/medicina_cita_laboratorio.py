# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaLaboratorioHistoria(models.Model) :
    _name = 'medicina.cita.laboratorio.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Laboratorio'
    
    laboratorio_abastonados_mm3 = fields.Float(string='''Abastonados (mm3)''')
    laboratorio_abastonados_porcentaje = fields.Float(string='''Abastonados (%)''')
    laboratorio_basofilos_mm3 = fields.Float(string='''Basofilos (mm3)''')
    laboratorio_basofilos_porcentaje = fields.Float(string='''Basofilos (%)''')
    laboratorio_bioquimica = fields.Boolean(string='''Bioquímica''')
    laboratorio_ccmh = fields.Integer(string='''CCMH (laboratorio)''')
    laboratorio_celulas_inmaduras = fields.Integer(string='''Celulas inmaduras''')
    laboratorio_colesterol_total = fields.Float(string='''Colesterol total''')
    laboratorio_comentarios = fields.Text(string='''Comentarios (laboratorio)''')
    laboratorio_eosinofilos_mm3 = fields.Float(string='''Eosinofilos (mm3)''')
    laboratorio_eosinofilos_porcentaje = fields.Float(string='''Eosinofilos (%)''')
    laboratorio_eritrocitos = fields.Integer(string='''Eritrocitos''')
    laboratorio_eritrosedimentacion = fields.Float(string='''Eritrosedimentacion (VSG)''')
    laboratorio_examen_quimico_acido_ascorbico = fields.Char(string='''Ácido ascórbico (examen químico)''')
    laboratorio_examen_quimico_bilirrubinas = fields.Char(string='''Bilirrubinas (examen químico)''')
    laboratorio_examen_quimico_cetonas = fields.Char(string='''Cetonas (examen químico)''')
    laboratorio_examen_quimico_nitritos = fields.Char(string='''Nitritos (examen químico)''')
    laboratorio_examen_quimico_ph = fields.Float(string='''pH (examen químico)''')
    laboratorio_examen_quimico_proteinas = fields.Char(string='''Proteínas (examen químico)''')
    laboratorio_examen_quimico_sangre = fields.Char(string='''Sangre (examen químico)''')
    laboratorio_examen_quimico_urobilinogeno = fields.Char(string='''Urobilinógeno (examen químico)''')
    laboratorio_factor_rh = fields.Selection(string='''Factor RH''',selection=[("positivo","+"),("negativo","-")])
    laboratorio_filamentos_mucosos = fields.Text(string='''Filamentos mucosos''')
    laboratorio_glucosa = fields.Float(string='''Glucosa''')
    laboratorio_grupo_sanguineo = fields.Selection(string='''Grupo sanguíneo''',selection=[("o","O"),("a","A"),("b","B"),("ab","AB")])
    laboratorio_hcm = fields.Integer(string='''HCM (laboratorio)''')
    laboratorio_hematocrito = fields.Float(string='''Hematocrito''')
    laboratorio_hemoglobina = fields.Float(string='''Hemoglobina''')
    laboratorio_leucocitos = fields.Integer(string='''Leucocitos''')
    laboratorio_linfocitos_mm3 = fields.Float(string='''Linfocitos (mm3)''')
    laboratorio_linfocitos_porcentaje = fields.Float(string='''Linfocitos (%)''')
    laboratorio_monocitos_mm3 = fields.Float(string='''Monocitos (mm3)''')
    laboratorio_monocitos_porcentaje = fields.Float(string='''Monocitos (%)''')
    laboratorio_orina_aspecto = fields.Char(string='''Aspecto de orina''')
    laboratorio_orina_color = fields.Char(string='''Color de orina''')
    laboratorio_orina_densidad = fields.Float(string='''Densidad de orina''')
    laboratorio_orina_examen_completo = fields.Boolean(string='''Examen completo de orina''')
    laboratorio_orina_examen_completo_resultado = fields.Selection(string='''Resultados del examen completo de orina''',selection=[("normal","Normal"),("anormal","Anormal")])
    laboratorio_recuento_plaquetas = fields.Integer(string='''Recuento de plaquetas''')
    laboratorio_resultados_glicemia = fields.Char(string='''Resultados de glicemia''')
    laboratorio_resultados_perfil_lipidico = fields.Char(string='''Resultados de perfil lipídico''')
    laboratorio_sedimento_bacterias = fields.Char(string='''Bacterias (sedimento)''')
    laboratorio_sedimento_celulas_epiteliales = fields.Char(string='''Células epiteliales (sedimento)''')
    laboratorio_sedimento_cilindros = fields.Char(string='''Cilindros (sedimento)''')
    laboratorio_sedimento_cristales = fields.Char(string='''Cristales (sedimento)''')
    laboratorio_sedimento_hematies = fields.Char(string='''Hematíes (sedimento)''')
    laboratorio_sedimento_leucocitos = fields.Char(string='''Leucocitos (sedimento)''')
    laboratorio_segmentados_mm3 = fields.Float(string='''Segmentados (mm3)''')
    laboratorio_segmentados_porcentaje = fields.Float(string='''Segmentados (%)''')
    laboratorio_trigliceridos = fields.Float(string='''Triglicéridos''')
    laboratorio_vcm = fields.Integer(string='''VCM (laboratorio)''')
    archivo_adjunto_laboratorio_1 = fields.Binary(string='''Archivo adjunto 1 (laboratorio)''')
    archivo_adjunto_laboratorio_1_filename = fields.Char(string='''Filename for archivo_adjunto_laboratorio_1''')
    archivo_adjunto_laboratorio_2 = fields.Binary(string='''Archivo adjunto 2 (laboratorio)''')
    archivo_adjunto_laboratorio_2_filename = fields.Char(string='''Filename for archivo_adjunto_laboratorio_2''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.laboratorio.historia''', relation='''medicina_cita_laboratorio_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaLaboratorio(models.Model) :
    _name = 'medicina.cita.laboratorio'
    _description = 'Cita de Laboratorio'
    _inherits = {'medicina.cita.laboratorio.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.laboratorio.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.laboratorio''', relation='''medicina_cita_laboratorio_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

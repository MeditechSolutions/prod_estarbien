# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaConfinados(models.Model) :
    _name = 'medicina.cita.confinados'
    _inherit = 'medicina.cita'
    _description = 'Cita de espacios confinados'
    
    confinados_alcoholismo_cronico = fields.Boolean(string='''Alcoholismo crónico''')
    confinados_alteracion_agudeza_visual = fields.Boolean(string='''Alteración de la agudeza visual''')
    confinados_alteracion_coordinacion = fields.Boolean(string='''Alteración de la coordinación presente (dedo, nariz)''')
    confinados_alteracion_equilibrio = fields.Boolean(string='''Alteración presente del equilibrio (Roemeberg)''')
    confinados_anemia = fields.Boolean(string='''Anemia según criterios OMS 2011''')
    confinados_anormalidad_marcha = fields.Boolean(string='''Anormalidad en la marcha con los ojos cerrados y/o abiertos''')
    confinados_anormalidad_musculo_esqueletico = fields.Boolean(string='''Anormalidad en la evaluación musculo-esquelética''')
    confinados_apnea = fields.Boolean(string='''Síndrome de apnea obstructiva del sueño''')
    confinados_aptitud_trabajo = fields.Selection(string='''Aptitud para trabajo en espacios confinados''',selection=[("no_apto","No apto"),("observado","Observado"),("apto_con_restriccion","Apto con restricción"),("apto","Apto")])
    confinados_arritmia_soplos = fields.Boolean(string='''Arritmia cardiaca o soplos''')
    confinados_campimetria_anormal = fields.Boolean(string='''Campimetría anormal (Test de confrontación alterada)''')
    confinados_claustrofobia = fields.Boolean(string='''Evaluación psicológica anormal (claustrofobia)''')
    confinados_comentarios_anamnesis = fields.Text(string='''Comentarios (anamnesis de espacios confinados)''')
    confinados_consume_estupefacientes = fields.Boolean(string='''Consume estupefacientes''')
    confinados_consume_estupefacientes_tratamiento = fields.Boolean(string='''Consume estupefacientes, pero está en tratamiento''')
    confinados_detalle_examen_fisico = fields.Text(string='''Detalle (examen físico de espacios confinados)''')
    confinados_detalle_medicinas = fields.Text(string='''Detalle de medicinas (espacios confinados)''')
    confinados_enfermedades_alteracion_consciencia = fields.Boolean(string='''Todas las enfermedades que produzcan alteración de la consciencia''')
    confinados_enfermedades_movimientos_involuntarios = fields.Boolean(string='''Movimientos involuntarios por enfermedad''')
    confinados_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (espacios confinados)''')
    confinados_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria (espacios confinados)''')
    confinados_hipoacusia = fields.Boolean(string='''Hipoacusia''')
    confinados_indice_masa_corporal = fields.Float(string='''Índice de masa corporal (espacios confinados)''', compute='''_compute_confinados_indice_masa_corporal''', store=True, readonly=False)
    confinados_lassegue_positivo = fields.Boolean(string='''Lassegue positivo''')
    confinados_limitacion_extremidades = fields.Boolean(string='''Limitación en fuerza y/o movilidad de extremidades''')
    confinados_nisfagmus = fields.Boolean(string='''Nisfagmus''')
    confinados_obesidad = fields.Boolean(string='''Obesidad''')
    confinados_otros_datos = fields.Text(string='''Otros datos relevantes (espacios confinados)''')
    confinados_perdida_recurrente_consciencia = fields.Boolean(string='''Pérdida recurrente de la consciencia''')
    confinados_peso = fields.Float(string='''Peso (espacios confinados)''')
    confinados_presion_arterial = fields.Char(string='''Presión arterial (espacios confinados)''')
    confinados_talla = fields.Integer(string='''Talla (espacios confinados)''')
    confinados_tratamiento_efectos_secundarios = fields.Boolean(string='''Efectos secundarios a causa de algún tratamiento''')
    confinados_validez_fin = fields.Date(string='''Fin de la validez de la aptitud (espacios confinados)''')
    confinados_validez_inicio = fields.Date(string='''Inicio de la validez de la aptitud (espacios confinados)''')
    confinados_vision_profundidad_alterada = fields.Boolean(string='''Prueba de visión de profundidad alterada''')
    
    @api.depends('confinados_talla','confinados_peso')
    def _compute_confinados_indice_masa_corporal(self):
        for rec in self:
            rec.confinados_indice_masa_corporal = rec.confinados_talla and rec.confinados_peso / ((rec.confinados_talla / 100.0) ** 2) or 0.0

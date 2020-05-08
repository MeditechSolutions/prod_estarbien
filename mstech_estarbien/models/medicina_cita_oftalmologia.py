# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaOftalmologia(models.Model) :
    _name = 'medicina.cita.oftalmologia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Oftalmología'
    
    oftalmologia_agudeza_agujero_con_correccion_derecho = fields.Integer(string='''Agudeza visual con el agujero estenopeico con corrección en el ojo derecho''')
    oftalmologia_agudeza_agujero_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual con el agujero estenopeico con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_agujero_sin_correccion_derecho = fields.Integer(string='''Agudeza visual con el agujero estenopeico sin corrección en el ojo derecho''')
    oftalmologia_agudeza_agujero_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual con el agujero estenopeico sin corrección en el ojo izquierdo''')
    oftalmologia_agudeza_cerca_con_correccion_derecho = fields.Integer(string='''Agudeza visual de cerca con corrección en el ojo derecho''')
    oftalmologia_agudeza_cerca_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual de cerca con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_cerca_sin_correccion_derecho = fields.Integer(string='''Agudeza visual de cerca sin corrección en el ojo derecho''')
    oftalmologia_agudeza_cerca_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual de cerca sin corrección en el ojo izquierdo''')
    oftalmologia_agudeza_lejos_con_correccion_derecho = fields.Integer(string='''Agudeza visual de lejos con corrección en el ojo derecho''')
    oftalmologia_agudeza_lejos_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual de lejos con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_lejos_sin_correccion_derecho = fields.Integer(string='''Agudeza visual de lejos sin corrección en el ojo derecho''')
    oftalmologia_agudeza_lejos_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual de lejos sin corrección en el ojo izquierdo''')
    oftalmologia_ambliopia = fields.Boolean(string='''Ambliopía''')
    oftalmologia_antecedentes_otros = fields.Text(string='''Otros''')
    oftalmologia_blefaritis_derecho = fields.Boolean(string='''Blefaritis en el ojo derecho''')
    oftalmologia_blefaritis_izquierdo = fields.Boolean(string='''Blefaritis en el ojo izquierdo''')
    oftalmologia_campimetria_derecho = fields.Char(string='''Campimetría del ojo derecho''')
    oftalmologia_campimetria_izquierdo = fields.Char(string='''Campimetría del ojo izquierdo''')
    oftalmologia_chalazion_derecho = fields.Boolean(string='''Chalazion en el ojo derecho''')
    oftalmologia_chalazion_izquierdo = fields.Boolean(string='''Chalazion en el ojo izquierdo''')
    oftalmologia_colores_derecho = fields.Char(string='''Visión de colores en el ojo derecho''')
    oftalmologia_colores_izquierdo = fields.Char(string='''Visión de colores en el ojo izquierdo''')
    oftalmologia_conjuntivitis_derecho = fields.Boolean(string='''Conjuntivitis en el ojo derecho''')
    oftalmologia_conjuntivitis_izquierdo = fields.Boolean(string='''Conjuntivitis en el ojo izquierdo''')
    oftalmologia_corrector_ocular_presente = fields.Boolean(string='''Presencia de corrector ocular''')
    oftalmologia_corrector_ocular_utiliza = fields.Boolean(string='''Uso de corrector ocular''')
    oftalmologia_dermatocalasia_derecho = fields.Boolean(string='''Dermatocalasia en el ojo derecho''')
    oftalmologia_dermatocalasia_izquierdo = fields.Boolean(string='''Dermatocalasia en el ojo izquierdo''')
    oftalmologia_diabetes = fields.Boolean(string='''Diabetes''')
    oftalmologia_estereopsis = fields.Char(string='''Estereopsis (oftalmología)''')
    oftalmologia_estrabismo_derecho = fields.Boolean(string='''Estrabismo en el ojo derecho''')
    oftalmologia_estrabismo_izquierdo = fields.Boolean(string='''Estrabismo en el ojo izquierdo''')
    oftalmologia_examen_externo_derecho = fields.Char(string='''Examen externo en el ojo derecho''')
    oftalmologia_examen_externo_izquierdo = fields.Char(string='''Examen externo en el ojo izquierdo''')
    oftalmologia_fondo_ojo = fields.Char(string='''Fondo de ojos''')
    oftalmologia_glaucoma = fields.Boolean(string='''Glaucoma''')
    oftalmologia_hipertension_arterial = fields.Boolean(string='''HTA''')
    oftalmologia_hipertension_ocular = fields.Boolean(string='''Hipertensión ocular''')
    oftalmologia_otros_anexos_derecho = fields.Boolean(string='''Otros anexos en el ojo derecho''')
    oftalmologia_otros_anexos_izquierdo = fields.Boolean(string='''Otros anexos en el ojo izquierdo''')
    oftalmologia_pterigium_derecho = fields.Boolean(string='''Pterigium en el ojo derecho''')
    oftalmologia_pterigium_izquierdo = fields.Boolean(string='''Pterigium en el ojo izquierdo''')
    oftalmologia_ptosis_derecho = fields.Boolean(string='''Ptosis en el ojo derecho''')
    oftalmologia_ptosis_izquierdo = fields.Boolean(string='''Ptosis en el ojo izquierdo''')
    oftalmologia_radiaciones = fields.Boolean(string='''Radiaciones''')
    oftalmologia_reflejo_pupila_derecho = fields.Char(string='''Reflejos pupilares en el ojo derecho''')
    oftalmologia_reflejo_pupila_izquierdo = fields.Char(string='''Reflejos pupilares en el ojo izquierdo''')
    oftalmologia_refraccion_cerca_derecho_cilindrico = fields.Char(string='''Refracción de cerca en el ojo derecho - cilindrico''')
    oftalmologia_refraccion_cerca_derecho_eje = fields.Char(string='''Refracción de cerca en el ojo derecho - eje''')
    oftalmologia_refraccion_cerca_derecho_esfera = fields.Char(string='''Refracción de cerca en el ojo derecho - esfera''')
    oftalmologia_refraccion_cerca_derecho_pupila = fields.Char(string='''Refracción de cerca en el ojo derecho - distancia entre pupilas''')
    oftalmologia_refraccion_cerca_izquierdo_cilindrico = fields.Char(string='''Refracción de cerca en el ojo izquierdo - cilindrico''')
    oftalmologia_refraccion_cerca_izquierdo_eje = fields.Char(string='''Refracción de cerca en el ojo izquierdo - eje''')
    oftalmologia_refraccion_cerca_izquierdo_esfera = fields.Char(string='''Refracción de cerca en el ojo izquierdo - esfera''')
    oftalmologia_refraccion_cerca_izquierdo_pupila = fields.Char(string='''Refracción de cerca en el ojo izquierdo - distancia entre pupilas''')
    oftalmologia_refraccion_lejos_derecho_cilindrico = fields.Char(string='''Refracción de lejos en el ojo derecho - cilindrico''')
    oftalmologia_refraccion_lejos_derecho_eje = fields.Char(string='''Refracción de lejos en el ojo derecho - eje''')
    oftalmologia_refraccion_lejos_derecho_esfera = fields.Char(string='''Refracción de lejos en el ojo derecho - esfera''')
    oftalmologia_refraccion_lejos_derecho_pupila = fields.Char(string='''Refracción de lejos en el ojo derecho - distancia entre pupilas''')
    oftalmologia_refraccion_lejos_izquierdo_cilindrico = fields.Char(string='''Refracción de lejos en el ojo izquierdo - cilindrico''')
    oftalmologia_refraccion_lejos_izquierdo_eje = fields.Char(string='''Refracción de lejos en el ojo izquierdo - eje''')
    oftalmologia_refraccion_lejos_izquierdo_esfera = fields.Char(string='''Refracción de lejos en el ojo izquierdo - esfera''')
    oftalmologia_refraccion_lejos_izquierdo_pupila = fields.Char(string='''Refracción de lejos en el ojo izquierdo - distancia entre pupilas''')
    oftalmologia_soldadura = fields.Boolean(string='''Soldadura''')
    oftalmologia_sustancias_quimicas = fields.Boolean(string='''Sustancias químicas''')
    oftalmologia_tonometria_derecho = fields.Char(string='''Tonometría del ojo derecho''')
    oftalmologia_tonometria_izquierdo = fields.Char(string='''Tonometría del ojo izquierdo''')
    oftalmologia_traumatismo = fields.Boolean(string='''Traumatismo''')
    oftalmologia_vision_nocturna = fields.Char(string='''Visión nocturna''')
    oftalmologia_vision_profundidad = fields.Char(string='''Visión de profundidad''')
    archivo_adjunto_oftalmologico_1 = fields.Binary(string='''Archivo adjunto 1 (oftalmológico)''')
    archivo_adjunto_oftalmologico_1_filename = fields.Char(string='''Filename for archivo_adjunto_oftalmologico_1''')
    archivo_adjunto_oftalmologico_2 = fields.Binary(string='''Archivo adjunto 2 (oftalmológico)''')
    archivo_adjunto_oftalmologico_2_filename = fields.Char(string='''Filename for archivo_adjunto_oftalmologico_2''')
    cie_10_oftalmologia_tipo_diagnostico = fields.Selection(string='''Tipo de diagnóstico CIE-10 oftalmológico''',selection=[("normal","Normal"),("anormal","Anormal")])

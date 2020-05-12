# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaAltura(models.Model) :
    _name = 'medicina.cita.altura'
    _inherit = 'medicina.cita'
    _description = 'Cita de Altura'
    
    altura_acrofobia = fields.Boolean(string='''Acrofobia (Temor a las alturas)''')
    altura_alcoholismo_adiccion = fields.Boolean(string='''Alcholismo o abuso de sustancias (adicción)''')
    altura_alteracion_coordinacion = fields.Boolean(string='''Alteración de la coordinación presente''')
    altura_anormalidades_fuerza_miembros = fields.Boolean(string='''Anormalidades en la fuerza de miembros''')
    altura_anormalidades_movimiento_ocular = fields.Boolean(string='''Anormalidades en movimiento ocular''')
    altura_antecedentes_entrevista_medicinas = fields.Text(string='''Medicinas que está tomando''')
    altura_antecedentes_medicos_comentario = fields.Text(string='''Comentario/Detalle''')
    altura_asimetria_facial = fields.Boolean(string='''Asimetría facial''')
    altura_cefalea_frecuencia = fields.Boolean(string='''Frecuencia de cefaleas''')
    altura_certificacion_aptitud = fields.Selection(string='''Aptitud para laborar por encima de 1.8 metros sobre el suelo''', selection=[("apto","Apto"),("no_apto","No apto"),("apto_restricciones","Apto con restricciones")])
    altura_certificacion_lentes = fields.Boolean(string='''Uso permanente de lentes correctores''')
    altura_certificacion_observaciones = fields.Text(string='''Observaciones / Recomendaciones''')
    altura_certificacion_otras_restricciones = fields.Char(string='''Otras restricciones''')
    altura_certificacion_protectores = fields.Boolean(string='''Uso permanente de protectores auditivos''')
    altura_certificacion_tipo = fields.Selection(string='''Tipo Certificación''', selection=[("primera_aptitud","Primera Aptitud"),("revalidacion","Revalidación")])
    altura_crisis_asmatica = fields.Boolean(string='''Crisis asmática''')
    altura_diabetes_hipoglicemia = fields.Boolean(string='''Diabetes mellitus o hipoglicemia no controlada''')
    altura_enfermedad_psiquiatrica = fields.Boolean(string='''Portador de enfermedad psiquiátrica''')
    altura_enfermedades_corazon = fields.Boolean(string='''Enfermedades del corazón''')
    altura_epilepsia_convulsiones_otros = fields.Boolean(string='''Pérdida de consciencia (epilepsia/convulsiones, otros)''')
    altura_equilibrio_alteracion = fields.Boolean(string='''Alteración del equilibrio''')
    altura_estereopsis_agudeza_visual = fields.Boolean(string='''Alteración de la agudeza visual (de lejos) y/o estereopsis''')
    altura_examen_fisico_detalles = fields.Text(string='''Detalles del examen físico''')
    altura_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca''')
    altura_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria''')
    altura_hipertension_arterial = fields.Boolean(string='''Hipertensión arterial no controlada''')
    altura_hipoacusia_severa = fields.Boolean(string='''Hipoacusia severa''')
    altura_inapto_labor_altura_previo = fields.Boolean(string='''INAPTO para labor de altura (según resultados previos)''')
    altura_indice_masa_corporal = fields.Float(string='''Índice de masa corporal''', compute='''_compute_altura_indice_masa_corporal''', store=True, readonly=False)
    altura_lenguaje_anormal = fields.Boolean(string='''Lenguaje anormal''')
    altura_licor_24_horas = fields.Boolean(string='''Consumió licor en las últimas 24 horas''')
    altura_limitacion_extremidades_fuerza_movilidad = fields.Boolean(string='''Limitación en fuerza y/o movilidad de extremidades''')
    altura_marcha_anormalidades = fields.Boolean(string='''Anormalidades en la marcha''')
    altura_migrana = fields.Boolean(string='''Migraña''')
    altura_nistagmus = fields.Boolean(string='''Nistagmus''')
    altura_peso = fields.Float(string='''Peso''')
    altura_presion_arterial = fields.Char(string='''Presión Arterial''')
    altura_pupilas_cirla = fields.Boolean(string='''Pupilas CIRLA''')
    altura_resfrio_cuadro_respiratorio = fields.Boolean(string='''Resfrío / Cuadro respiratorio''')
    altura_saturacion_oxigeno = fields.Float(string='''Saturación de Oxígeno''')
    altura_talla = fields.Float(string='''Talla''')
    altura_vertigo_mareo = fields.Boolean(string='''Vértigo / Mareos recientes''')
    
    @api.depends('altura_talla','altura_peso')
    def _compute_altura_indice_masa_corporal(self):
        for rec in self:
            rec.altura_indice_masa_corporal = rec.altura_talla and rec.altura_peso / (rec.altura_talla ** 2) or 0.0
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.altura.historia''')
    
    @api.model
    def create(self, values) :
        res = super(MedicinaCitaAltura, self).create(values)
        if self._name == 'medicina.cita.altura' :
            values.update({'original_id': res.id})
            valores = self.env['medicina.cita.altura.historia'].create(values)
        return res
    
    def write(self, vals) :
        res = super(MedicinaCitaAltura, self).write(vals)
        if self._name == 'medicina.cita.altura' :
            valores = self.env['medicina.cita.altura.historia'].search([('original_id','in',self.ids)]).write(vals)
        return res

class MedicinaCitaAlturaHistoria(models.Model) :
    _name = 'medicina.cita.altura.historia'
    _inherit = 'medicina.cita.altura'
    
    original_id = fields.Many2one(comodel_name='medicina.cita.altura', string='Origen cita')
    

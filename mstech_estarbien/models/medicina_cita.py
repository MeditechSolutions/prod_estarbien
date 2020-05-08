# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaPacientePerfil(models.Model) :
    _name = 'medicina.paciente.perfil'
    _description = 'Perfil de paciente'
    
    name = fields.Char(string='''Perfil''')

class MedicalPatient(models.Model) :
    _inherit = 'medical.patient'
    
    perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''',string='''Perfil''')

class MedicinaCita(models.Model) :
    _name = 'medicina.cita'
    _description = 'Cita'
    
    tipo_cita = fields.Selection(string='''Tipo''',selection=[("diagnostico","Diagnóstico"),
                                                              ("triaje","Triaje"),
                                                              ("antecedentes_personales","Antecedentes Personales"),
                                                              ("historia_ocupacional","Historia Ocupacional"),
                                                              ("medicina","Medicina general"),
                                                              ("dermatologia","Dermatología"),
                                                              ("grandes_alturas","Anexo N°16 A"),
                                                              ("altura","Certificación de trabajo en altura"),
                                                              ("confinados","Trabajo en espacios confinados"),
                                                              ("electrocardiograma","Electrocardiograma"),
                                                              ("oftalmologia","Oftalmología"),
                                                              ("audiometria","Audiometría"),
                                                              ("psicologia","Psicología"),
                                                              ("odontograma","Odontograma"),
                                                              ("musculo_esqueletico","Músculo Esquelético"),
                                                              ("radiologia","Radiología"),
                                                              ("espirometria","Espirometría"),
                                                              ("tsr","Test de Sintomático Respiratorio"),
                                                              ("laboratorio","Laboratorio"),
                                                              ("consentimiento","Consentimiento"),
                                                              ("interconsultas","Interconsultas"),
                                                              ("encuesta","Encuesta")])
    fecha_cita = fields.Date(string='''Fecha''')
    paciente_id = fields.Many2one(comodel_name='''medical.patient''', string='''Paciente''')
    atencion_inicio = fields.Datetime(string='''Inicio de la atención''')
    atencion_fin = fields.Datetime(string='''Fin de la atención''')
    
    paciente_apellidos_nombres = fields.Char(string='''Apellidos y nombres''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_cargo = fields.Char(string='''Cargo''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_dni = fields.Char(string='''DNI''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_edad = fields.Char(string='''Edad''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_empresa_id = fields.Many2one(comodel_name='''res.partner''', string='''Empresa''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''', string='''Perfil''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_sexo = fields.Selection(string='''Sexo''',selection=[('m', 'Male'),('f', 'Female')], compute='''_compute_paciente_datos''', store=True, readonly=True)
    tipo_examen_salud_ocupacional = fields.Selection(string='''Tipo de Examen de Salud Ocupacional''',selection=[("empo","EMPO"),("emoa","EMOA"),("emor","EMOR")])
    
    @api.depends('paciente_id')
    def _compute_paciente_datos(self):
        for record in self :
            record.paciente_apellidos_nombres = record.paciente_id.patient_id.name
            record.paciente_cargo = record.paciente_id.patient_id.function
            record.paciente_dni = record.paciente_id.patient_id.vat
            record.paciente_edad = record.paciente_id.age
            record.paciente_sexo = record.paciente_id.sex
            record.paciente_empresa_id = record.paciente_id.partner_address_id
            record.paciente_perfil_id = record.paciente_id.perfil_id
    
    auditado = fields.Boolean(string='''Auditado''')
    auditor = fields.Many2one(comodel='''res.partner''', string='''Auditor''')
    responsable = fields.Many2one(comodel='''res.partner''', string='''Responsable''')
    revisado = fields.Boolean(string='''Revisado''')
    medico = fields.Many2one(comodel='''res.partner''', string='''Médico''')
    evaluador = fields.Many2one(comodel='''res.partner''', string='''Evaluador''')
    
    diagnostico_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico''', domain=[('tipo_diagnostico_oido','=','bilateral')])
    diagnostico_oido_derecho_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido derecho''', domain=[('tipo_diagnostico_oido','=','derecho')])
    diagnostico_oido_izquierdo_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido izquierdo''', domain=[('tipo_diagnostico_oido','=','izquierdo')])
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita''', relation='''medicina_cita_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')
    
    name = fields.Char(string='''Cita''')

class MedicinaCitaDiagnostico(models.Model) :
    _name = 'medicina.cita.diagnostico'
    _description = 'Diagnóstico de la cita'
    
    cita_id = fields.Many2one(comodel_name='''medicina.cita''', string='''Cita origen''', ondelete='''cascade''')
    tipo_diagnostico_oido = fields.Selection(string='''Tipo de diagnóstico (oído)''', selection=[("bilateral","Bilateral"),("derecho","Derecho"),("izquierdo","Izquierdo")], default='''bilateral''')
    codigo_cie_10 = fields.Char(string='''Código CIE-10 del diagnóstico''')
    descripcion = fields.Char(string='''Descripción del diagnóstico''')
    recomendaciones = fields.Char(string='''Recomendaciones del diagnóstico''')

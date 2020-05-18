# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaOdontogramaHistoria(models.Model) :
    _name = 'medicina.cita.odontograma.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Odontología'
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.odontograma.historia''', relation='''medicina_cita_odontograma_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaOdontograma(models.Model) :
    _name = 'medicina.cita.odontograma'
    _description = 'Cita de Odontología'
    _inherits = {'medicina.cita.odontograma.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.odontograma.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.odontograma''', relation='''medicina_cita_odontograma_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

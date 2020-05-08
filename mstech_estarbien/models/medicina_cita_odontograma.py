# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaOdontograma(models.Model) :
    _name = 'medicina.cita.odontograma'
    _inherit = 'medicina.cita'
    _description = 'Cita de Odontología'
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.odontograma''', relation='''medicina_cita_odontograma_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

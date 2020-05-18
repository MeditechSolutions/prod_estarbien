# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaRadiologiaHistoria(models.Model) :
    _name = 'medicina.cita.radiologia.historia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Radiología'
    
    radiologia_comentario = fields.Text(string='''Comentario (radiología)''')
    archivo_adjunto_radiologia_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_radiologia_1_filename = fields.Char(string='''Filename for archivo_adjunto_radiologia_1''')
    
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.radiologia.historia''', relation='''medicina_cita_radiologia_historia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

class MedicinaCitaRadiologia(models.Model) :
    _name = 'medicina.cita.radiologia'
    _description = 'Cita de Radiología'
    _inherits = {'medicina.cita.radiologia.historia': 'original_id'}
    
    original_id = fields.Many2one(comodel_name='medicina.cita.radiologia.historia')
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita.radiologia''', relation='''medicina_cita_radiologia_m2m_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')

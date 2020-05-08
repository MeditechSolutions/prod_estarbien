# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaRadiologia(models.Model) :
    _name = 'medicina.cita.radiologia'
    _inherit = 'medicina.cita'
    _description = 'Cita de Radiología'
    
    radiologia_comentario = fields.Text(string='''Comentario (radiología)''')
    archivo_adjunto_radiologia_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_radiologia_1_filename = fields.Char(string='''Filename for archivo_adjunto_radiologia_1''')

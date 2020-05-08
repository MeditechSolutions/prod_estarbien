# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaTSR(models.Model) :
    _name = 'medicina.cita.tsr'
    _inherit = 'medicina.cita'
    _description = 'Cita de Test Sintomático-Respiratorio'
    
    test_sr_baja_peso_inexplicable = fields.Boolean(string='''Baja de peso inexplicable''')
    test_sr_conclusion = fields.Boolean(string='''Conclusión''')
    test_sr_familiares_amigos_tuberculosis = fields.Boolean(string='''Familiares o amigos con tuberculosis''')
    test_sr_observaciones = fields.Text(string='''Observaciones''')
    test_sr_resultado_bk_esputo_1 = fields.Text(string='''Resultado de Bk de Esputo 1°''')
    test_sr_resultado_radiografia_torax = fields.Text(string='''Resultado de radiografía de tórax''')
    test_sr_sospecha_tuberculosis = fields.Boolean(string='''Sospecha de tuberculosis''')
    test_sr_sudoracion_nocturna_importante = fields.Boolean(string='''Sudoración nocturna importante''')
    test_sr_tos_mas_15_dias = fields.Boolean(string='''Tos por más de 15 días''')
    test_sr_tos_sangre = fields.Boolean(string='''Tos con sangre''')
    test_sr_tuberculosis = fields.Boolean(string='''Tuberculosis''')

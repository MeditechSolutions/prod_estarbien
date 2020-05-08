# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicinaCitaOdontograma(models.Model) :
    _name = 'medicina.cita.odontograma'
    _inherit = 'medicina.cita'
    _description = 'Cita de Odontología'

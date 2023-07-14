from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class ResUsersInherit(models.Model):
    _inherit = 'res.users'

    def write(self, values):
        user = self.env.user
        if not user.has_group('base.group_hr_employee'):
        #if not user.has_group('account.group_account_invoice'):
            raise UserError(_('No tiene permiso para editar este usuario, comuniquese con el administrador o con los encargados de recursos humanos.'))

        res = super(ResUsersInherit, self).write(values)
        return res

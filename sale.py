#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.

from trytond.model import Workflow, ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class Invoice(ModelSQL, ModelView):
    _name = 'account.invoice'

    @Workflow.transition('draft')
    def draft(self, ids):
        '''Available cancel invoices from sale'''
        pass

Invoice()

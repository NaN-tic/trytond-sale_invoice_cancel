#This file is part sale_invoice_cancel module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, Workflow
from trytond.pool import Pool, PoolMeta

__all__ = ['Invoice']
__metaclass__ = PoolMeta

class Invoice:
    __name__ = 'account.invoice'

    @classmethod
    @ModelView.button
    @Workflow.transition('draft')
    def draft(cls, invoices):
        '''Available cancel invoices from purchase'''
        pass



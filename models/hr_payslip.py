# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.onchange('employee_id', 'date_from', 'date_to')
    def _onchange_employee(self):
        """
        تجاوز الربط التلقائي للعقد الأوحد لجلب العقود النشطة للموظف 
        والسماح باختيار العقد المطلوب يدوياً دون إجبار النظام على عقد واحد.
        """
        res = super(HrPayslip, self)._onchange_employee()
        
        if self.employee_id and self.date_from and self.date_to:
            contracts = self.employee_id._get_contracts(self.date_from, self.date_to, states=['open', 'close'])
            if contracts:
                # تصفية النطاق ليظهر للمستخدم جميع عقود الموظف النشطة في القائمة
                return {'domain': {'contract_id': [('id', 'in', contracts.ids)]}}
        return res

    def _get_contract_search_domain(self):
        """
        تأكيد البحث عن العقود المتاحة خلال فترة قسيمة الراتب
        """
        domain = super(HrPayslip, self)._get_contract_search_domain()
        return domain
from odoo import http, fields
from odoo.http import request
from odoo.addons.web.controllers.report import ReportController


class CustomReportController(ReportController):

    @http.route([
        '/report/<converter>/<reportname>',
        '/report/<converter>/<reportname>/<docids>',
    ], type='http', auth='user', website=True)
    def report_routes(self, reportname, docids=None, converter=None, **data):
        if reportname == 'hr_hospital.doctor_report_template':
            old_report_footer = request.env.company.report_footer
            request.env.company.report_footer = """<p>Printed %s %s</p>""" % (
                fields.Date.today(), request.env.company.city)
        res = super(CustomReportController, self).report_routes(reportname, docids, converter, **data)
        if reportname == 'hr_hospital.doctor_report_template':
            request.env.company.report_footer = old_report_footer
        return res

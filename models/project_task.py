# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Task(models.Model):
    _inherit = 'project.task'

    slot_ids = fields.One2many('planning.slot', 'task_id', string='Project Task Slot')

    def _prepare_project_task_shift(self):
        for task in self:
            employees = task.user_ids.mapped('employee_id')
            PlanningSlot = self.env['planning.slot']
            slot = PlanningSlot.search([('task_id', '=', task.id)])
            if not slot:
                if employees and task.sale_line_id and task.project_id and task.planned_date_begin and task.planned_date_end and task.planned_date_end > task.planned_date_begin:
                    task.slot_ids = PlanningSlot.create([{
                        'resource_id': employee.id,
                        'role_id': employee.planning_role_ids[0].id if employee.planning_role_ids else False,
                        'task_id': task.id,
                        'project_id': task.project_id.id,
                        'sale_line_id': task.sale_line_id.id,
                        'start_datetime': task.planned_date_begin,
                        'end_datetime': task.planned_date_end,
                        'is_task_shift': True,
                    } for employee in employees])

        for slot in self.slot_ids:
            if not slot.allocated_percentage > 100.0:
                slot.action_publish()

    @api.model_create_multi
    def create(self, vals_list):
        tasks = super().create(vals_list)
        tasks._prepare_project_task_shift()
        return tasks

    def write(self, vals):
        res = super().write(vals)
        to_update_shift = {}
        if 'user_ids' in vals:
            for task in self:
                if task.slot_ids:
                    task.slot_ids.unlink()
                task._prepare_project_task_shift()

        elif 'stage_id' in vals:
            for task in self:
                if task.is_closed and task.slot_ids:
                    to_update_shift['end_datetime'] = vals['date_last_stage_update']
                    task.slot_ids.write(to_update_shift)

        else:
            if 'project_id' in vals:
                to_update_shift['project_id'] = vals['project_id']
            if 'sale_line_id' in vals:
                to_update_shift['sale_line_id'] = vals['sale_line_id']
            if 'planned_date_begin' in vals:
                to_update_shift['start_datetime'] = vals['planned_date_begin']
            if 'planned_date_end' in vals:
                to_update_shift['end_datetime'] = vals['planned_date_end']
            for task in self:
                if task.slot_ids:
                    task.slot_ids.write(to_update_shift)
        return res

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields


class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    is_task_shift = fields.Boolean('Task Shift')

    @api.depends('allocated_hours', 'start_datetime', 'end_datetime')
    def _compute_allocated_percentage(self):
        slots_from_task = self.filtered(lambda slot: slot.is_task_shift)
        for slot in slots_from_task:
            number_of_users = len(slot.task_id.user_ids) if slot.task_id.user_ids else 1
            slot.allocated_percentage = ((slot.task_id.planned_hours) / ((slot.task_id.planned_date_end - slot.task_id.planned_date_begin).total_seconds() / 3600.0)) / number_of_users
        super(PlanningSlot, self - slots_from_task)._compute_allocated_percentage()

    @api.depends('start_datetime', 'sale_line_id.planning_hours_to_plan', 'sale_line_id.planning_hours_planned', 'task_id.planned_hours')
    def _compute_allocated_hours(self):
        slots_from_task = self.filtered(lambda slot: slot.is_task_shift)
        for slot in slots_from_task:
            number_of_users = len(slot.task_id.user_ids) if slot.task_id.user_ids else 1
            slot.allocated_hours = slot.task_id.planned_hours / number_of_users
        super(PlanningSlot, self - slots_from_task)._compute_allocated_hours()

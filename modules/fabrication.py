from reactpy import component, html, utils, hooks, event
from modules.navbar import NavBar
from modules.form import InputTaskForm, DeleteTaskIdForm, AddConstructionStatusForm
from modules.sqlmodeldb import add_fabrication_status, select_all_tasks, select_task_by_task_name
# from modules.task import TaskView
import pandas as pd


@component
def FabStatusForm():
    task_name, set_task_name = hooks.use_state('')
    status, set_status = hooks.use_state('')  # task progress in percentage like 25 for 25%
    comment, set_comment = hooks.use_state('')
    created_by, set_created_by = hooks.use_state('')

    def save_record(event):
        add_fabrication_status(task_name, float(status), comment, created_by)

    return html.form(
        {'on_submit': save_record},
        html.div(
            {'class': 'mb-3'},
            html.label({'for': 'task', 'class': 'form-label fw-bold mt-3'}, 'Task name'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'task',
                    'value': task_name, 'placeholder': 'input task name', 
                    'on_change': lambda event: \
                      set_task_name(event['target']['value'])
                }
            ),
            html.label({'for': 'status', 'class': 'form-label fw-bold mt-3'}, 'Task status'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'status',
                    'value': status, 'placeholder': 'input task status', 
                    'on_change': lambda event: \
                      set_status(event['target']['value'])
                }
            ),
            html.label({'for': 'comment', 'class': 'form-label fw-bold mt-3'}, 'Comment'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'comment',
                    'value': comment, 'placeholder': 'input comment', 
                    'on_change': lambda event: \
                      set_comment(event['target']['value'])
                }
            ),            
            html.label({'for': 'created_by', 'class': 'form-label fw-bold mt-3'}, 'Created by'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'created_by',
                    'value': created_by, 'on_change': lambda event: \
                      set_created_by(event['target']['value'])
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit', 'value': 'Save'}
            )
        )
    )


# @component
# def InputFabStatus():
    # return html.div(
        # html.div(
            # {'class': 'container mt-3'},
            # NavBar({'Task': True}),

            # html.div({'class': 'fs-5 fw-bold mt-3 text-success'}, 'Input Fabrication Status'),
            # html.p('Add fabrication status in a given task name.'),
            # FabStatusForm(),

            # html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            # TaskView(),
        # )
    # )
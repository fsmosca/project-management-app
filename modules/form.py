from reactpy import component, html, hooks
from modules.sqlmodeldb import add_task, delete_task, add_fabrication_status, add_construction_status


@component
def InputTaskForm():
    task_name, set_task_name = hooks.use_state('')
    task_created_by, set_task_created_by = hooks.use_state('')

    def save_record(event):
        add_task(task_name, task_created_by)

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
            html.label({'for': 'created_by', 'class': 'form-label fw-bold mt-3'}, 'Created by'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'created_by',
                    'value': task_created_by, 'on_change': lambda event: \
                      set_task_created_by(event['target']['value'])
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit', 'value': 'Save'}
            )
        )
    )


@component
def DeleteTaskIdForm():
    task_name, set_task_name = hooks.use_state('')

    def delete_record(event):
        delete_task(task_name)

    return html.form(
        {'on_submit': delete_record},
        html.div(
            {'class': 'mb-3'},
            html.label({'for': 'task_name', 'class': 'form-label fw-bold mt-3'}, 'Task name'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'task_name',
                    'value': task_name, 'placeholder': 'input task name to delete', 
                    'on_change': lambda event: \
                      set_task_name(event['target']['value'])
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit', 'value': 'Delete task'}
            )
        )
    )


@component
def AddConstructionStatusForm():
    task_name, set_task_name = hooks.use_state('')

    def update_construction_status(event):
        add_construction_status(task_name)

    return html.form(
        {'on_submit': update_construction_status},
        html.div(
            {'class': 'mb-3'},
            html.label({'for': 'taskname', 'class': 'form-label fw-bold mt-3'}, 'Task name'),
            html.input(
                {
                    'class': 'form-control', 'type': 'text', 'id': 'taskname',
                    'value': task_name, 'placeholder': 'input task name', 
                    'on_change': lambda event: set_task_name(event['target']['value'])
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit', 'value': "Add Construction status"}
            )
        )
    )
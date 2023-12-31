from reactpy import component, html, hooks
from modules.sqlmodeldb import add_construction_status
from modules.navbar import NavBar
from modules.task import TaskView


@component
def ConstructionStatusForm():
    task_name, set_task_name = hooks.use_state('')
    date, set_date = hooks.use_state('')
    progress, set_progress = hooks.use_state('')
    status, set_status = hooks.use_state('')
    note, set_note = hooks.use_state('')
    created_by, set_created_by = hooks.use_state('')

    def save_record(event):
        add_construction_status(
            task_name,
            date,
            created_by,
            status,
            float(progress),
            note
        )

    return html.form(
        {'on_submit': save_record},
        html.div(
            {'class': 'mb-3'},
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col'},
                    html.label(
                        {'for': 'task', 'class': 'form-label fw-bold mt-3'},
                        'Task name'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'text',
                            'id': 'task',
                            'value': task_name,
                            'placeholder': 'input task name',
                            'on_change': lambda event:
                                set_task_name(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col'},
                    html.label(
                        {'for': 'date', 'class': 'form-label fw-bold mt-3'},
                        'Status date'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'date',
                            'id': 'date',
                            'value': date,
                            'placeholder': 'input date',
                            'on_change': lambda event:
                                set_date(event['target']['value'])
                        }
                    )
                )
            ),
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col'},
                    html.label(
                        {
                            'for': 'progress',
                            'class': 'form-label fw-bold mt-3'
                        },
                        'Task progress'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'text',
                            'id': 'progress',
                            'value': progress,
                            'placeholder': 'input task progress',
                            'on_change': lambda event:
                                set_progress(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col'},
                    html.label(
                        {'for': 'status', 'class': 'form-label fw-bold mt-3'},
                        'Task status'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'text',
                            'id': 'status',
                            'value': status,
                            'placeholder': 'input task status',
                            'on_change': lambda event:
                                set_status(event['target']['value'])
                        }
                    )
                )
            ),
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col'},
                    html.label(
                        {'for': 'note', 'class': 'form-label fw-bold mt-3'},
                        'Note'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'text',
                            'id': 'note',
                            'value': note,
                            'placeholder': 'input note',
                            'maxlength': '50',
                            'on_change': lambda event:
                                set_note(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col'},
                    html.label(
                        {
                            'for': 'created_by',
                            'class': 'form-label fw-bold mt-3'
                        },
                        'Recorded by'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'text',
                            'id': 'created_by',
                            'value': created_by,
                            'on_change': lambda event:
                                set_created_by(event['target']['value'])
                        }
                    )
                )
            ),
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col'},
                    html.input(
                        {
                            'class': 'btn btn-primary my-3',
                            'type': 'submit',
                            'value': 'Save'
                        }
                    )
                )
            )
        )
    )


@component
def AddConstructionStatus():
    return html.div(
        html.div(
            {'class': 'container mt-5 pt-3'},
            NavBar({'Construction': True}),

            html.div(
                {'class': 'fs-5 fw-bold text-danger'},
                'Construction Status'
            ),
            html.p('Adds construction status by task name.'),
            ConstructionStatusForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView()
        )
    )

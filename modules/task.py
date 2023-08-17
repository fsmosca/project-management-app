from typing import Optional

from reactpy import component, html, utils, hooks, event
from modules.navbar import NavBar
from modules.form import InputTaskForm, DeleteTaskIdForm, AddConstructionStatusForm
from modules.sqlmodeldb import select_all_tasks, select_task_by_task_name
from modules.fabrication import FabStatusForm
import pandas as pd


def find_task(task_name: str = '') -> pd.DataFrame:
    """Search row given task name."""
    dataframe = []
    if task_name is not None:
        db_records_by_name = select_task_by_task_name(task_name)
    all_records = db_records_by_name
    for rec in all_records:
        row_val = row_to_dict(rec)
        dataframe.append(row_val)
    df = pd.DataFrame(dataframe)
    return df


def row_to_dict(row):
    """Converts an sqlite data row into a python dictionary."""
    out = {}
    for column in row.__table__.columns:
        out[column.name] = str(getattr(row, column.name))

    return out


@component
def TaskView():
    """Transfrom sqlite data into html."""
    dataframe = []
    db_records = select_all_tasks()
    for rec in db_records:
        v = row_to_dict(rec)
        dataframe.append(v)
    df = pd.DataFrame(dataframe)

    html_rec = df.to_html(
        index=False,
        border=0,
        justify='center',
        classes=[
            'table', 'table-primary',
            'table-bordered', 'text-center',
            'table-striped', 'table-hover'
        ]
    )

    return html.div(
        {
            'class': 'mt-2',
            'style': {
                'height': '300px',
                'overflow-y': 'auto',
            }
        },
        utils.html_to_vdom(html_rec)
    )


@component
def SearchResult(df):
    html_rec = df.to_html(
        index=False,
        border=0,
        justify='center',
        classes=[
            'table', 'table-primary',
            'table-bordered', 'text-center',
            'table-striped', 'table-hover'
        ]
    )

    return html.div(
        {
            'class': 'mt-2',
            'style': {
                'overflow-y': 'auto',
            }
        },
        utils.html_to_vdom(html_rec)
    )


@component
def SearchTaskForm():
    search_task_name, set_search_task_name = hooks.use_state('')
    search_df, set_search_df = hooks.use_state(pd.DataFrame())

    @event(prevent_default=True)
    def search_record(event):
        df = pd.DataFrame()
        if search_task_name != '':
            df = find_task(search_task_name)
            set_search_df(df)

    return html.form(
        {'on_submit': search_record},
        html.div(
            {'class': 'mb-3'},
            html.label(
                {'for': 'taskname', 'class': 'form-label fw-bold mt-3'},
                'Task name'
            ),
            html.input(
                {
                    'class': 'form-control',
                    'type': 'text',
                    'id': 'taskname',
                    'value': search_task_name,
                    'placeholder': 'input task name', 
                    'on_change': lambda event: set_search_task_name(event['target']['value']),
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit', 'value': 'Search task'}
            ),

            html.div({'class': 'fs-5 fw-bold mt-3 text-primary'}, 'Search Result'),
            SearchResult(search_df)
        )
    )


@component
def SearchTask():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Task': True}),
            html.div({'class': 'fs-5 fw-bold mt-3 text-info'}, 'Search Task'),
            html.p('Enter your task name to get info about it.'),
            SearchTaskForm()
        )
    )


@component
def InputTask():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Task': True}),

            html.div({'class': 'fs-5 fw-bold mt-3 text-success'}, 'Input Task'),
            html.p('Unique task id will be automatically generated.'),
            InputTaskForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView(),
        )
    )


@component
def DeleteTask():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Task': True}),

            html.div({'class': 'fs-5 fw-bold mt-3 text-danger'}, 'Delete Task'),
            html.p('Enter task name to delete.'),
            DeleteTaskIdForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView()
        )
    )


@component
def AddFabricationStatus():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Fabrication': True}),

            html.div({'class': 'fs-5 fw-bold mt-3 text-danger'}, 'Fabrication Status'),
            html.p('Adds fabrication status by task name.'),
            FabStatusForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView()
        )
    )


@component
def AddConstructionStatus():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Construction': True}),

            html.div({'class': 'fs-5 fw-bold mt-3 text-danger'}, 'Construction Status'),
            html.p('Adds construction status by task name.'),
            AddConstructionStatusForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView()
        )
    )

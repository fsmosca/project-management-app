from typing import List
import pandas as pd
from reactpy import component, html, utils, hooks, event

from modules.navbar import NavBar
from modules.sqlmodeldb import (add_task, select_all_tasks,
                                select_task_by_task_name, Task)


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


def sqlitedb_to_df(db_records: List[Task]) -> pd.DataFrame:
    dict_frame = [row_to_dict(rec) for rec in db_records]
    return pd.DataFrame(dict_frame)


@component
def TaskView():
    """Transfrom sqlite data into html."""
    df = sqlitedb_to_df(select_all_tasks())
    return html.div(DataframeToVdom(df))


@component
def DataframeToVdom(df):
    """Converts a pandas dataframe into ReactPy VDOM."""
    html_rec = df.to_html(
        index=False,
        border=0,
        justify='center',
        classes=['table', 'text-nowrap', 'table-bordered',
                 'text-center', 'table-striped', 'table-hover',
                 'table-primary']
    )
    return html.div(
        html.style("""
        .table-fix-head {
            overflow-y: auto;
            height: 200px;
        }
        .table-fix-head table {
            border-collapse: collapse;
            width: 100%;
        }
        .table-fix-head th,
        .table-fix-head td {
            padding: 8px 16px;
        }
        .table-fix-head th {
            position: sticky;
            top: 0;
            background: #97BDC4;
        }
        """),
        html.div(
            {'class': 'table-fix-head'},
            utils.html_to_vdom(html_rec)
        )
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
                    'on_change': lambda event: \
                        set_search_task_name(event['target']['value']),
                }
            ),
            html.input(
                {'class': 'btn btn-primary my-3', 'type': 'submit',
                 'value': 'Search task'}
            ),

            html.div({'class': 'fs-5 fw-bold mt-3 text-primary'},
                     'Search Result'),
            DataframeToVdom(search_df)
        )
    )


@component
def SearchTask():
    return html.div(
        html.div(
            {'class': 'container mt-5 pt-3'},
            NavBar({'Task': True}),

            html.div({'class': 'fs-5 fw-bold text-info'}, 'Search Task'),
            html.p('Enter your task name to get info about it.'),
            SearchTaskForm()
        )
    )


@component
def InputTaskForm():
    task_name, set_task_name = hooks.use_state('')
    task_date, set_task_date = hooks.use_state('')
    task_created_by, set_task_created_by = hooks.use_state('')

    def save_record(event):
        add_task(task_name, task_date, task_created_by)

    return html.form(
        {'on_submit': save_record},
        html.div(
            {'class': 'mb-3'},
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col-4'},            
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
                            'maxlength': '50',
                            'on_change': lambda event: \
                              set_task_name(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col-3'},
                    html.label(
                        {'for': 'date', 'class': 'form-label fw-bold mt-3'},
                        'Task date'
                    ),
                    html.input(
                        {
                            'class': 'form-control',
                            'type': 'date',
                            'id': 'date',
                            'value': task_date,
                            'placeholder': 'input task date', 
                            'on_change': lambda event: \
                              set_task_date(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col-3'},
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
                            'maxlength': '50',
                            'type': 'text',
                            'id': 'created_by',
                            'value': task_created_by,
                            'on_change': lambda event: \
                              set_task_created_by(event['target']['value'])
                        }
                    )
                ),
                html.div(
                    {'class': 'col-2'},
                    html.div({'class': 'mb-5'}),
                    html.input(
                        {'class': 'btn btn-primary mb-4', 'type': 'submit',
                         'value': 'Save'}
                    )
                )
            )
        )
    )


@component
def InputTask():
    return html.div(
        html.div(
            {'class': 'container mt-5 pt-3'},
            NavBar({'Task': True}),

            html.div({'class': 'fs-5 fw-bold text-success'}, 'Input Task'),
            html.p('Unique table id will be automatically generated.'),
            InputTaskForm(),

            html.div({'class': 'fs-5 fw-bold my-3 text-primary'}, 'Task View'),
            TaskView(),
        )
    )

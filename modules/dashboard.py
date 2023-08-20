from io import StringIO

from reactpy import component, html, utils
from modules.navbar import NavBar
from modules.task import sqlitedb_to_df, DataframeToVdom
from modules.sqlmodeldb import select_all_tasks
import plotly.express as px
import pandas as pd


LABEL = 'Dashboard'


LINE_COLOR = {'Fabrication': 'blue', 'Construction': 'red'}


def fabrication_progress(df, num_lines):
    fab_cnt = len(df.loc[(df['category'] == 'Fabrication')
                         & (df['status'] == 'DONE')])
    return round(100 * fab_cnt / num_lines, 2)


def construction_progress(df, num_lines):
    con_cnt = len(df.loc[(df['category'] == 'Construction') &
                         (df['status'] == 'DONE')])
    return round(100 * con_cnt / num_lines, 2)


@component
def LineChart(df, category, width=500, height=250):
    df1 = df.copy()
    df1['recorded_date'] = pd.to_datetime(df1['recorded_date'])
    df1['week_number'] = df1['recorded_date'].dt.isocalendar().week
    df1 = df1.astype({'progress': float})
    df2 = df1.loc[(df1['category'] == category) & (df1['status'] == 'DONE')]
    df3 = df2.groupby(by=['week_number'])['task_name'].count().reset_index()
    df3['weekly_progress'] = df3['task_name'] / 12 * 100
    df3['progress_%'] = df3['weekly_progress'].cumsum()

    # Create a figure using the grouped dataframe.
    fig = px.line(
        df3, x='week_number', y='progress_%', markers=True,
        width=width, height=height, title=category
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=100, b=20),
        paper_bgcolor="#CEF5AF",
    )

    fig.update_traces(line_color=LINE_COLOR[category], line_width=1)

    # Create an html object in memory from fig.
    buffer = StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    fig_html = buffer.getvalue()

    return html.div(utils.html_to_vdom(fig_html))


@component
def BarChart(df, width=500, height=250):
    """Creates a plotly bar chart."""
    fig = px.bar(
        df, x='progress_%', y='category', orientation='h', color='category',
        width=width, height=height, text_auto=True,
        title='Fabrication and Construction'
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=100, b=20),
        paper_bgcolor="#CEF5AF",
    )

    fig.update_yaxes(visible=False, showticklabels=False)

    # Create an html object in memory from fig.
    buffer = StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    fig_html = buffer.getvalue()

    return html.div(
        utils.html_to_vdom(fig_html)
    )


def LineStatus(df):
    return DataframeToVdom(df)


def LineHoldStatus(df):
    return DataframeToVdom(df)


@component
def Summary():
    df = sqlitedb_to_df(select_all_tasks())
    if len(df) < 1:
        return
    gb = df.groupby('task_name')
    current_line_status = gb.last().reset_index()
    num_lines = len(current_line_status)

    # Plot fabrication and construction progress.
    fab_done_pct = fabrication_progress(df, num_lines)
    con_done_pct = construction_progress(df, num_lines)
    progress_dict = {
        'category': ['Fabrication', 'Construction'],
        'progress_%': [fab_done_pct, con_done_pct]
    }
    df_fab_con_progress = pd.DataFrame(progress_dict)

    # Task with hold current status.
    df_hold = current_line_status.loc[current_line_status['status'] == 'HOLD']

    return html.div(
        html.div(
            {'class': 'container'},
            html.div(
                {'class': 'row'},
                html.div(
                    {'class': 'col'},
                    html.h5(
                        {'class': 'mt-1'},
                        'Overall Progress'
                    ),
                    BarChart(df_fab_con_progress, 400)
                ),
                html.div(
                    {'class': 'col'},
                    html.h5(
                        {'class': 'mt-1'},
                        'Fabrication Weekly Cummulative Progress'
                    ),
                    LineChart(df, 'Fabrication', 400)
                ),
                html.div(
                    {'class': 'col'},
                    html.h5(
                        {'class': 'mt-1'},
                        'Construction Weekly Cummulative Progress'
                    ),
                    LineChart(df, 'Construction', 400)
                )
            ),
            html.div(
                {'class': 'row'},
                html.h5({'class': 'mt-3'}, 'Line current status'),
                LineStatus(current_line_status)
            ),
            html.div(
                html.h5({'class': 'mt-3'}, 'Lines with HOLD status'),
                LineHoldStatus(df_hold)
            )
        )
    )


@component
def DashboardContent():
    return html.div(
        Summary()
    )


@component
def Dashboard():
    return html.div(
        html.div(
            {'class': 'container'},
            NavBar({'Dashboard': True}),
            html.div(
                html.div(
                   {'class': 'fw-bold fs-5 mt-5 py-3 text-center'},
                   LABEL
                ),
                DashboardContent()
            )
        )
    )

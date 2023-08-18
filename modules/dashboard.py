from reactpy import component, html
from modules.navbar import NavBar
from modules.task import sqlitedb_to_df, DataframeToVdom
from modules.sqlmodeldb import select_all_tasks


LABEL = 'Dashboard'


@component
def Linelist():
    df = sqlitedb_to_df(select_all_tasks())
    gb = df.groupby('task_name')
    gbr = gb.last().reset_index()

    gbr = gbr.astype({'progress': float})

    # Fabrication
    dffc = gbr.loc[gbr['category'] == 'Construction']
    dff = gbr.loc[gbr['category'] == 'Fabrication']
    total_progress = dff['progress'].sum() + 100 * len(dffc)
    fabrication_pct_complete = round(100*total_progress / (100 * len(gbr)), 2)

    # Construction
    dfc = gbr.loc[(gbr['category'] == 'Construction') & (gbr['progress'] >= 100)]
    construction_pct_complete = round(100 * len(dfc) / len(gbr), 2)

    return html.div(
        DataframeToVdom(gbr, height=200),
        html.p({'class': 'mt-3'}, f'Fabrication Completion: {fabrication_pct_complete} %'),
        html.p({'class': 'mt-3'}, f'Construction Completion: {construction_pct_complete} %')
    )


@component
def DashboardContent():
    return html.div(
        html.div(
            {'class': 'fw-bold fs-5 my-3'},
            LABEL
        ),
        html.p('This is the latest status of each line.'),
        Linelist(),
    )


@component
def Dashboard():
    return html.div(
        html.div(
            {'class': 'container mt-4 pt-4'},
            NavBar({'Dashboard': True}),
            DashboardContent()
        ),
    )

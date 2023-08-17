from reactpy import component, html
from modules.navbar import NavBar


LABEL = 'Home'


@component
def Home_1():
    title = 'PMA - Project Management App'
    return html.div(
        {'style': {'font-family': 'monospace'}},
        html.h1(title),
        html.h2('A. Introduction'),
        html.p(
           '''Effective project management is essential for successfully
           finishing a project. This involves documenting tasks and issues,
           monitoring task advancement, and systematically addressing any
           problems that arise.'''
        ),

        html.h2('B. Features'),
        html.ul(
            html.li('Input tasks and save to a sqlite database.'),
            html.li('Add and save status and comments for each task to easier track the issues.'),
            html.li('Can delete tasks.'),
            html.li('Display progress charts.'),
            html.li('more ...')
        )
    )


@component
def HomeContent():
    return html.div(
        html.div(
            {'class': 'fw-bold fs-5 my-3'},
            LABEL
        ),
        Home_1(),
    )


@component
def Home():
    return html.div(
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Home': True}),
            HomeContent()
        ),
    )

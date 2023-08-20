from reactpy import component, html
from modules.navbar import NavBar


LABEL = 'Blog'


@component
def Blog_1():
    title = 'Application Guide'
    return html.div(
        {'style': {'font-family': 'monospace'}},
        html.h1(title),

        html.h2('A. Tasks'),
        html.p(
            '''The navigation bar located at the top of the page has Home,
            Blog, Task, Fabrication and Construction menu.'''
        ),
        html.ul(
            html.li('''Task - is a dropdown that contents
                    "search task" and "input task".'''),
            html.li('''Fabrication - is also a dropdown dealing with
                    fabrication-related interfaces.''')
        ),

        html.h3('1. Search Task'),
        html.p('''This is used to search tasks.'''),

        html.h3('2. Input Task'),
        html.p('''This is used to register the task in the sqlite database.
                Task name must be unique.'''),
    )


@component
def BlogContent():
    return html.div(
        html.div(
            {'class': 'fw-bold fs-5 my-3'},
            LABEL
        ),
        Blog_1()
    )


@component
def Blog():
    return html.div(
        html.div(
            {'class': 'container mt-4 pt-4'},
            NavBar({'Blog': True}),
            BlogContent()
        ),
    )

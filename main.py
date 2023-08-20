"""This module contains the main entry point of the application."""


from reactpy import component, html
from reactpy_router import route, simple
from reactpy.backend.fastapi import configure, Options
from fastapi import FastAPI
from modules.sqlmodeldb import create_db_and_tables
from modules.home import Home
from modules.blog import Blog
from modules.missing import MissingLink
from modules.task import SearchTask, InputTask
from modules.fabrication import AddFabricationStatus
from modules.construction import AddConstructionStatus
from modules.dashboard import Dashboard
from modules.bootstrap import BOOTSTRAP_CSS, BOOTSTRAP_SCRIPT
from modules.plotly import PLOTLY_JS


PAGE_HEADER_TITLE = 'Project Management App'


create_db_and_tables()


@component
def Root():
    return simple.router(
        route('/', Home()),
        route('/blog', Blog()),
        route('/search-task', SearchTask()),
        route('/input-task', InputTask()),
        route('/fabrication-status', AddFabricationStatus()),
        route('/construction-status', AddConstructionStatus()),
        route('/dashboard', Dashboard()),
        route('*', MissingLink())
    )


app = FastAPI()
configure(
    app,
    Root,
    options=Options(
        head=html.head(
            html.link(BOOTSTRAP_CSS),
            html.script(BOOTSTRAP_SCRIPT),
            html.script(PLOTLY_JS),
            html.title(PAGE_HEADER_TITLE)
        )
    )
)

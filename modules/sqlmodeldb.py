from typing import Optional
from pathlib import Path

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_name: str = ''
    recorded_date: str = ''
    recorded_by: str = ''
    category: str= ''  # Register, Fabrication, Construction
    status: str = ''  # STARTED, WPI, HOLD, DONE
    progress: float = 0.0
    note: str = ''

sqlite_file_name = "tasks.sqlite"
sqlite_url = f"sqlite:///data/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    folder_path = Path.cwd() / 'data'
    folder_path.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)


def add_task(task_name:str, recorded_date: str, recorded_by: str):
    """Adds task to the table.

    Duplicate task name is automatically detected and is not saved.
    """
    if len(select_task_by_task_name(task_name)):
        return
    
    task = Task(
        task_name=task_name,
        recorded_date=recorded_date,
        recorded_by=recorded_by,
        category='Register',
        status='DONE',
        progress=100.0
    )

    with Session(engine) as session: 
        session.add(task)
        session.commit()


def select_all_tasks():
    """Gets all records from the table."""
    with Session(engine) as session:
        statement = select(Task)
        results = session.exec(statement)
        return results.all()
    

def select_task_by_id(id_: int):
    """Select task by id."""
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id_)
        results = session.exec(statement)
        return results.all()
    

def select_task_by_task_name(task_name: str):
    """Select task by task_name."""
    with Session(engine) as session:
        statement = select(Task).where(Task.task_name == task_name)
        results = session.exec(statement)
        return results.all()


def add_fabrication_status(
        task_name: str,
        recorded_date: str,
        recorded_by: str,
        status: str,
        progress: float,        
        note: str
    ):
    task = Task(
        task_name=task_name,
        recorded_date=recorded_date,
        recorded_by=recorded_by,
        category='Fabrication',        
        status=status,
        progress=progress,
        note=note
    )

    with Session(engine) as session: 
        session.add(task)
        session.commit()


def add_construction_status(
        task_name: str,
        recorded_date: str,
        recorded_by: str,
        status: str,
        progress: float,        
        note: str
    ):
    task = Task(
        task_name=task_name,
        recorded_date=recorded_date,
        recorded_by=recorded_by,
        category='Construction',        
        status=status,
        progress=progress,
        note=note
    )

    with Session(engine) as session: 
        session.add(task)
        session.commit()


def select_latest_task_status():
    """Select all tasks but show only the latest status."""
    all_tasks = select_all_tasks()
  
  

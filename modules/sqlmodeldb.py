from typing import Optional
from pathlib import Path

from datetime import datetime, timezone

from sqlmodel import Field, Session, SQLModel, create_engine, select
import sqlalchemy


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_name: str = ''
    task_rec_date: str = ''
    task_rec_by: str = ''
    fabric_prog: float = 0.0
    fabric_status: str = ''
    fabric_date: str = ''
    fabric_note: str = ''
    fabric_rec_by: str = ''
    constr_prog: float = 0.0
    constr_status: str = ''
    constr_date: str = ''
    constr_note: str = ''
    constr_rec_by: str = ''


sqlite_file_name = "tasks.sqlite"
sqlite_url = f"sqlite:///data/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    folder_path = Path.cwd() / 'data'
    folder_path.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)


def add_task(task_name:str, task_date: str, task_rec_by: str):
    """Adds task to the table.

    Duplicate task name is automatically detected and is not saved.
    """
    if len(select_task_by_task_name(task_name)):
        return
    
    task = Task(
        task_name=task_name,
        task_rec_date=task_date,
        task_rec_by=task_rec_by
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


def delete_task(task_name: int):
    """Deletes an entry from a given id."""
    pass
    # with Session(engine) as session:
        # statement = select(Task).where(Task.task_name == task_name)
        # results = session.exec(statement)

        # try:
            # task = results.one()
        # except sqlalchemy.exc.NoResultFound:
            # pass
        # except Exception as err:
            # print(repr(err))
        # else:
            # session.delete(task)
            # session.commit()


def add_fabrication_status(
        task_name:str,
        fabric_date:str,
        fabric_prog:float,
        fabric_status:str,
        fabric_note:str,
        fabric_rec_by: str,
    ):
    task = Task(
        task_name=task_name,
        fabric_date=fabric_date,  # datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        fabric_prog=fabric_prog,
        fabric_status=fabric_status,        
        fabric_note=fabric_note,
        fabric_rec_by=fabric_rec_by
    )

    with Session(engine) as session: 
        session.add(task)
        session.commit()


def add_construction_status(
        task_id: int,
        task_name:str,
        task_rec_date: str,
        task_rec_by: str,
    ):
    task = Task(
        task_name=task_name,
        task_rec_date=task_rec_date,
        task_rec_by=task_rec_by
    )

    with Session(engine) as session: 
        session.add(task)
        session.commit()

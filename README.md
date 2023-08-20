# Project Management App

This app is created using [ReactPy](https://reactpy.dev/docs/guides/getting-started/index.html). This is used to record the progress and issues in a simplified fabrication and construction activities in an oil and gas typical project. Data is stored in sqlite database utilizing the [SQLModel](https://sqlmodel.tiangolo.com/) libary.

The database is in the 'data' folder. The reactpy components are in the modules folder. There are task.py, fabrication.py, construction.py and other modules. The components are inside these modules.

## A. Dashboard

Check progress and issues.

![image](https://github.com/fsmosca/project-management-app/assets/22366935/c4e31108-ad72-400c-9b05-9e7093e528b5)

## B. Input task

Add task in input-task page.

![image](https://github.com/fsmosca/project-management-app/assets/22366935/8ce4bc44-668e-48ad-8ec3-5894f8ac5b75)

### C. Search task

Examine the history of the task.

![image](https://github.com/fsmosca/project-management-app/assets/22366935/f2feb962-b91e-4db5-adbd-425a9004e413)

## D. Add task update on fabrication works

![image](https://github.com/fsmosca/project-management-app/assets/22366935/16b2f339-c416-4df0-b6f8-e1d2ce0f1048)

## E. Add construction update

![image](https://github.com/fsmosca/project-management-app/assets/22366935/f22088df-3e0d-41d2-8d3b-bb3f8c5b329c)

## F. Setup

Clone the repository.

```
git clone https://github.com/fsmosca/project-management-app.git
```

Change directory to `project-mamangement-app` and run the command:

```
uvicorn main:app
```

## G. Credits

* [ReactPy](https://reactpy.dev/docs/guides/getting-started/index.html)
* [Pandas](https://pandas.pydata.org/)
* [SQLModel](https://sqlmodel.tiangolo.com/)
* [Plotly](https://plotly.com/python/)

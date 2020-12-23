# python_todo_clean_api
This project manage code related to Python example of clean architecture API

## What is clean architecture

Clean architecture is a code separation principle enforcing a clean distinction between
products usecases, object representation, internal code and transport to user. 

In each couch, every module needs to stand alone, reposing only on upper couch modules.

In this example, we organize code as follows:

- **domains** represent an object transported in the application. It is not the object a user, nor the database will see.
- **modules** regroup all functional code required for running the project.
- **usecases** regroup all product expressed features. No functional code should be here,
    as this couch only link user transport entry with correct **modules** to provide a product
    feature to the end user.
- **transport** regroup all interfaces available to the user.

Learn more about clean architecture here: [Explaining clean architecture, oncehub]([clean-architecture])

## Run the project

### Flask

- Clone the project: `git clone https://github.com/switchelven/python_todo_clean_api.git`
- Install dependencies: `pip install -r requirement.txt`
- Run: `./run_flask.py`
- Check project running: [localhost:5000](localhost:5000)
- Check endpoints: [localhost:5000/routes](localhost:5000/routes)

## Modules

### IO

IO modules provides methods to abstract file manipulation from python code. It is 
mainly used to load endpoints from transports.

### logger

Provides and simple and clean structure to log information from requests.

### Registry

Registry manages a local server store for each request.

### Sqlite

SQLite implements Flask SQLAlchemy models definitions for SQLite.

### Tasks

Represent a task as a database model and provides simple functional methods required
for usecases.

## Domains

### Task

Task domain represent a task inside the system and provides method to serialize tasks 
to user.

## Usecases

### Tasks

Regroup all product usecases related to task

#### Create


## Transport

### Flasks

Implements flask transport and describes endpoints. 
Endpoints retrieve user entry, convert it to domains then call correct usecase
and provides formatted response to user.



[clean-architecture]: https://www.oncehub.com/blog/explaining-clean-architecture

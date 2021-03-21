# Issue Tracker
> An issue tracking system that manages and maintains lists of issues.

# Parts of an projects
* Name
* Short name (slug)
* Status (In progress, Success, Cancel)

# Parts of an issue
* Summary
* Description
* Type (Tasks/Bugs)
* Priority (Low, Medium, High)
* Status (To do, In progress, Done, Cancel)
* Attachments
* Reporter
* Assignee
* Comments
* Unique issue number

## Technologies
* Python 3.9
* Django 3.1.6
* PostgreSQL
* Docker


## Setup
All information about environment you can find in requirements.txt

Clone project:
```bash
git clone https://github.com/efefre/issue_tracker.git
```
Use:
* [Docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

Run project:
```bash
make start
```

Makemigrations:
```bash
make makemigrations
```

Migrate:
```bash
make migrate
```

Create super user (root):
```bash
make createsuperuser
```

Open:
```bash
127.0.0.1:8000
```

_More details about [make](https://github.com/efefre/issue_tracker/blob/master/Makefile)_.


## Frontend
Base on AdminLTE https://adminlte.io/docs/3.0/license.html (an open source project that is licensed under the MIT license).


## Status
Project is: _no longer continue_.


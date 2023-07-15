# Django Project About Workers

During the development of the project, both basics and additional conditions were met. More on this later.

## Quick Start

First of all you need to get the project on your PC

    git clone git@github.com:vladdemo1/demo_working_output.git

After that, if necessary, creates a virtual environment to run this project

    python3 -m venv working_output_venv

Next, in an already open project, start the virtual environment with the following command

    source /home/<UR_NAME>/venvs/working_output_venv/bin/activate

Install required dependencies

    pip install -r requirements.txt

Now go to the 'workers' directory where 'manage.py' is located

    cd workers/

For reliability, run migrations

    python manage.py makemigrations

    python manage.py migrate

Congratulations! Now you can run the project with the following command

    python manage.py runserver


## What was been done and how to view it

### Main part

- A worker model has been created with the required fields, [you can view it here](https://github.com/vladdemo1/demo_working_output/blob/master/workers/api/models.py)
- The database has been populated with over 50.000 workers with 7 hierarchies
- The position of the worker is displayed in a black frame on his pisture
- Bootstrap was used

### Main page

The main page can be viewed at the [following address](http://127.0.0.1:8000/)

    http://127.0.0.1:8000/

The base page displays a director who has subordinate workers that are rendered lazy.

Each worker card is active, by clicking on it, you can get to detailed information about a worker.

## What has been done additionally

### A django-seed was used to filling the database with workers

To comply with more than 50,000 workers in DB and 7 hierarhies, the number 6 to the power 7 was chosen.

An additional condition was met when filling the database. Used [django-seed](https://pypi.org/project/django-seed/).

These commands have already been used, they DO NOT NEED to be entered

At the first filling, the command was used:

    python manage.py seed api --number=1 --seeder "Worker.position" "Chief Director"

At the second filling, the command was used:

    python manage.py seed api --number=6 --seeder "Worker.position" "Deputy Director"

At the third filling, the command was used:

    python manage.py seed api --number=36 --seeder "Worker.position" "Head of department"

At the fourth filling, the command was used:

    python manage.py seed api --number=216 --seeder "Worker.position" "Deputy Head"

At the fifth filling, the command was used:

    python manage.py seed api --number=1296 --seeder "Worker.position" "Laboratory assistant"

At the sixth filling, the command was used:

    python manage.py seed api --number=7776 --seeder "Worker.position" "Pharmacist"

At the seventh filling, the command was used:

    python manage.py seed api --number=46656 --seeder "Worker.position" "Security Guard"

A total of 55987 workers were added to the database.

### Workers search by any field was added

[Being on the main page](http://127.0.0.1:8000/)

    http://127.0.0.1:8000/

In the search field, you can enter the word ...

    Lyons

... and fild workers for this query

### Lazy loading of workers was added

4 cards each, using the build-in Paginator

[For example](http://127.0.0.1:8000/positions/chief/1/)

    http://127.0.0.1:8000/positions/chief/1/

### A drop-down list with positions

A drop-down list has been added where you can select a position and get a random worker

### Mobile friendly

Templates are also suitable for mobile devices and adapt to screen sizes

### Worker Detail

By clicking on any worker, you can get to his detailed information

[For example](http://127.0.0.1:8000/worker-detail/Pharmacist/Catherine/King/)

    http://127.0.0.1:8000/worker-detail/Pharmacist/Catherine/King/

# I didn't have time to do it, but somehow I did it

## List of all workers

Here it would be possible to use a regular View and a Paginator for 8 cards on page

## User autentication

For this, there is already a blank on the front side, it would be necessary to do the following:

- Create user model
- Create a view for registration and login
- Customize access to the front part

## CRUD

For this, there is already a blank on the front side, it would be necessary to do the following:

- Set up views for selecting and working with the worker, manipulation, etc.

# What was used in the development of the project

## OS

    Linux Ubuntu 22.04.02 LTS

## Text editor

    VS Code

## Git

    GitHub

## Programming language

    Python

## Web

    HTML CSS jQuery JS Bootstrap

## Framework

    Django


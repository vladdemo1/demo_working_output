# Django Project About Workers

During the development of the project, both basics and additional conditions were met. More on this later.

## Filling the database with workers

To comply with more than 50,000 workers in DB and 7 hierarhies, the number 6 to the power 7 was chosen.

An additional condition was met when filling the database. Used [django-seed](https://pypi.org/project/django-seed/).

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


import os
from unipath import Path
import sys

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent

sys.path.append(root_dir)
os.chdir(root_dir)

from DEV._clear_migrations import do_clear_migrations
from DEV._load_fixtures import do_load_fixtures


## only need this stuff if you want to run Django functions
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetDevOps.settings')
# from NetDevOps import settings as DJANGO_SETTINGS_MODULE
# import django
# django.setup()
# from django.contrib.auth.models import User

do_clear_migrations()
db_filename = "db.sqlite3"


if os.path.exists(db_filename):
    print("Removing DB file: %s" % db_filename)
    os.remove(db_filename)
else:
    print("The DB file %s does not exist" % db_filename)

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
do_load_fixtures()

# User.objects.create_superuser('admin', 'admin@example.com', 'admin')
os.system("python manage.py runserver")

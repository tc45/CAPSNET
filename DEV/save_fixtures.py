import os

from unipath import Path

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent
dev_dir = root_dir + '/DEV'
os.chdir(root_dir)

os.system("python manage.py dumpdata --indent 4 auth > " + dev_dir + "/fixtures/last/auth.json")
os.system("python manage.py dumpdata --indent 4 dashboard > " + dev_dir + "/fixtures/last/dashboard.json")
os.system("python manage.py dumpdata --indent 4 devices > " + dev_dir + "/fixtures/last/devices.json")
os.system("python manage.py dumpdata --indent 4 templates > " + dev_dir + "/fixtures/last/templates.json")
os.system("python manage.py dumpdata --indent 4 provisioning > " + dev_dir + "/fixtures/last/provisioning.json")
os.system("python manage.py dumpdata --indent 4 tools > " + dev_dir + "/fixtures/last/tools.json")
os.system("python manage.py dumpdata --indent 4 reports > " + dev_dir + "/fixtures/last/reports.json")
os.system("python manage.py dumpdata --indent 4 settings > " + dev_dir + "/fixtures/last/settings.json")

import os
from unipath import Path

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent
dev_dir = root_dir + '/DEV'
os.chdir(root_dir)


def do_load_fixtures():
    os.system("python manage.py loaddata --app auth " + dev_dir + "/fixtures/last/auth.json")
    os.system("python manage.py loaddata --app dashboard " + dev_dir + "/fixtures/last/dashboard.json")
    os.system("python manage.py loaddata --app devices " + dev_dir + "/fixtures/last/devices.json")
    os.system("python manage.py loaddata --app templates " + dev_dir + "/fixtures/last/templates.json")
    os.system("python manage.py loaddata --app provisioning " + dev_dir + "/fixtures/last/provisioning.json")
    os.system("python manage.py loaddata --app tools " + dev_dir + "/fixtures/last/tools.json")
    os.system("python manage.py loaddata --app reports " + dev_dir + "/fixtures/last/reports.json")
    os.system("python manage.py loaddata --app settings " + dev_dir + "/fixtures/last/settings.json")


# def main():
#     do_load_fixtures()


# main()

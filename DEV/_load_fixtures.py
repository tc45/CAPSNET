import os
from unipath import Path

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent
dev_dir = root_dir + '/DEV'
os.chdir(root_dir)

file_dict = {}
file_dict['auth'] = dev_dir + "/fixtures/last/auth.json"
file_dict['appsettings'] = dev_dir + "/fixtures/last/appsettings.json"
file_dict['dashboard'] = dev_dir + "/fixtures/last/dashboard.json"
file_dict['devices'] = dev_dir + "/fixtures/last/devices.json"
file_dict['apptemplates'] = dev_dir + "/fixtures/last/apptemplates.json"
file_dict['provisioning'] = dev_dir + "/fixtures/last/provisioning.json"
file_dict['tools'] = dev_dir + "/fixtures/last/tools.json"
file_dict['reports'] = dev_dir + "/fixtures/last/reports.json"



def do_load_fixtures():
    for appname, filename in file_dict.items():
        filesize = os.path.getsize(filename)
        if filesize < 10:
            print(filename + " - is empty.  Skipping import")
        else:
            print("Found data for app: " + appname + ".  Loading file: " + filename)
            os.system("python manage.py loaddata --app " + appname + " " + filename)


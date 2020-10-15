import os

from unipath import Path

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent
dev_dir = root_dir + '/DEV'
os.chdir(root_dir)

file_dict = {}
file_dict['auth'] = dev_dir + "/fixtures/last/auth.json"
file_dict['dashboard'] = dev_dir + "/fixtures/last/dashboard.json"
file_dict['devices'] = dev_dir + "/fixtures/last/devices.json"
file_dict['apptemplates'] = dev_dir + "/fixtures/last/apptemplates.json"
file_dict['provisioning'] = dev_dir + "/fixtures/last/provisioning.json"
file_dict['tools'] = dev_dir + "/fixtures/last/tools.json"
file_dict['reports'] = dev_dir + "/fixtures/last/reports.json"
file_dict['appsettings'] = dev_dir + "/fixtures/last/appsettings.json"


# Cycle through file dictionary and dump data for each app into JSON file
for appname, filename in file_dict.items():
    print("Saving app " + appname + " to file " + filename)
    os.system("python manage.py dumpdata --indent 4 " + appname + " > " + filename)

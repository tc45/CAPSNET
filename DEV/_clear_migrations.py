"""
Removes all migration files from all apps in a Django project.
"""
from unipath import Path

this_file = Path(__file__).absolute()
root_dir = this_file.parent.parent
dir_list = root_dir.listdir()

def is_private_file(filename):
    if filename[0:2] == "__":
        return True
    else:
        return False


def is_migration_file(filename):
    if is_private_file(filename):
        return False
    else:
        if filename[-2:] == "py":
            if filename[0:1] == "0":
                return True


def do_clear_migrations():
    for path in dir_list:
        migration_folder = path.child('migrations')
        if migration_folder.exists():
            list_files = migration_folder.listdir()
            for file in list_files:
                split = file.components()
                filename = split[-1]
                if is_migration_file(filename):
                    print("deleting file: " + str(filename))
                    file.remove()
                else:
                    print("ignoring file: " + str(filename))
    return


# def main():
#     do_clear_migrations()
#
# main()

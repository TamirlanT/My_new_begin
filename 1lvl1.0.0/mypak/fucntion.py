import os

def make_new_dir(name, count):
    for i in range(1,count + 1):
        new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        os.mkdir(new_path)

def deldir(name, count):
    for i in range(1, count + 1):
        os.rmdir('{}_{}'.format(name, i))

# make_new_dir('dir', 10)
# deldir('dir', 10)

import importlib
import os
import shutil
import subprocess

DBFILE = 'db.sqlite3'


# Wipe out old database and migrations
if os.path.exists(DBFILE):
    os.remove(DBFILE)

for d in os.listdir('.'):
    path = os.path.join(d, 'migrations')
    if os.path.exists(path):
        shutil.rmtree(path)


# Create database
subprocess.call(['python3', 'manage.py', 'createsuperuser'])
subprocess.call(['python3', 'manage.py', 'migrate'])
subprocess.call(['python3', 'manage.py', 'makemigrations', 'enquirer'])
subprocess.call(['python3', 'manage.py', 'migrate', 'enquirer', '0001'])


# Make users
#p = subprocess.Popen(['python3', 'manage.py', 'shell' ], stdin=subprocess.PIPE)
#p.stdin.write("""
#from django.contrib.auth.models import User
#user = User.objects.create(username="johannes.tax@gmx.at", password="johannes", first_name="Johannes", last_name="Tax")
#""".encode('utf-8'))
#p.communicate()


# Add tests
for testname in os.listdir('tests'):
    if not os.path.exists(os.path.join('tests', testname)):
        continue
    testname = os.path.splitext(testname)[0]
    test = importlib.import_module('tests.%s' % testname)
    test.Test().setup()

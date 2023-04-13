import sys
sys.path.append('/home/jae/myprj/mysite')  #  Python search 디렉토리 경로 추가

# To use Django objects in the file which are not created from startapps command, add DJANGO_SETTING_MODULE to the system environemnt 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from daq.models import Tnh

def save_db(msg):
    db_tab1 = Tnh()
    db_tab1.temperature = float(msg.topic)
    db_tab1.humidity = float(msg.payload)

    print(db_tab1.temperature, db_tab1.humidity)

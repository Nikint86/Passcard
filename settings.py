from dotenv import load_dotenv
import os
load_dotenv()

engine = os.environ["ENGINE"]
host = os.environ["HOST"]
port = os.environ["PORT"]
name = os.environ["NAME"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]

DATABASES = {
    'default': {
        'ENGINE': engine,
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

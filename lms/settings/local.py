from .base import *

SECRET_KEY = 'znm&^q$l5&6!c2gc807)@3)6y@v!t2+@o!o(k8i^eh6d&nd0b-'
DEBUG = True

VARIABLES = {
    'SITE_NAME': '無線網際網路實驗室',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}

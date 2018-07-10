ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'polla',
        'USER': 'polla',
        'PASSWORD': 'polla',
        'HOST': '127.0.0.1',
    }
}

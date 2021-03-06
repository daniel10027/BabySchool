"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import dj_database_url # heroku
# import django_heroku # heroku

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3-suu@bmeyw=w&(vmj5%i=*pkhoyf!0#x955tx4a+m*zwajtfd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'test-app-proto.herokuapp.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # new!
    'django.contrib.staticfiles',

    # third apps
    'crispy_forms',
    'memcache_status',        
    'debug_toolbar',

    # Local Apps
    'accounts.apps.AccountsConfig',
    'students.apps.StudentsConfig',
    'teachers.apps.TeachersConfig',
    'schools.apps.SchoolsConfig',
    'courses.apps.CoursesConfig',
    'pages.apps.PagesConfig',
    'grade.apps.GradeConfig'

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # new!

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # django debug toolbar

]
INTERNAL_IPS = ('127.0.0.1', )  # debug toolbar

CACHES = {
'default': {
'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
'LOCATION': '127.0.0.1:11211',
}
}
ROOT_URLCONF = 'mysite.urls'
AUTH_USER_MODEL = 'accounts.User'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'teachers.processors.course_owned_by_user',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
        'default':{
         'ENGINE':'django.db.backends.postgresql',
         'NAME':'sms',
         'USER':'sms',
         'PASSWORD':'sms',
         'HOST':'localhost',
         'PORT':''
     }

 }

db_from_env = dj_database_url.config(conn_max_age=500) # heroku
DATABASES['default'].update(db_from_env) # he
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new!
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # new!


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



#Authentication
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGOUT_REDIRECT_URL = reverse_lazy('account:login')



#Caching
# CACHES = {
#     'default': {
#     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#     'LOCATION': '/tmp/memcached.sock'
 
#     # 'LOCATION': '127.0.0.1:65535',
#     }
# }


# CACHES = {
#     'default':{
#         'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION':'127.0.0.1:11211'
#     }
# }
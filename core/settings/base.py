from pathlib import Path

from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Add extra '.parent' because I'm using directory based settings management
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Environment variables
ENV = config('ENV', default='development', cast=str)
DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY', default='$2b$12$H.uDdnSIoQ/5RkXq9HlDaO9uKQwq5epdvskn%t)dfqseM9z1EKldYa')

ALLOWED_HOSTS = []
extend_allowed_hosts = config('ALLOWED_HOSTS', default='localhost, 127.0.0.1')
if extend_allowed_hosts is not None:
    # remove spaces around the host and add it to the allowed hosts
    ALLOWED_HOSTS.extend(list(map(str.strip, extend_allowed_hosts.split(','))))

# Email server setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_SERVER_HOST')
EMAIL_PORT = config('EMAIL_SERVER_PORT')
EMAIL_USE_SSL = config('EMAIL_SERVER_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = '<{}>'.format(EMAIL_HOST_USER)

# Database server setup
DB_NAME = config('DB_NAME')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_USE_EXTERNAL = config('USE_EXTERNAL_DB', default=False, cast=bool)

SHOW_STARTUP_DETAILS = config('SHOW_STARTUP_DETAILS', default=False, cast=bool)

if SHOW_STARTUP_DETAILS:
    print("DEVELOPMENT SERVER STARTING...\n\tENV: {}\n\tDEBUG: {}".format(ENV, DEBUG))
    print("EMAIL SERVER:\n\tHOST: {}\n\tPORT: {}".format(EMAIL_HOST, EMAIL_PORT))
    print("\tUSER: {}\n\tSSL/TLS: {}".format(EMAIL_HOST_USER, EMAIL_USE_SSL))
    print("DB SERVER:\n\tNAME: {}\n\tHOST: {}\n\tPORT: {}\n\tUSER: {}".format(DB_NAME, DB_HOST, DB_PORT, DB_USERNAME))
    print("ALLOWED_HOSTS: ", ALLOWED_HOSTS)
    print("\n")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # applications
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if DB_USE_EXTERNAL:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Use 'users.models.CustomUser' model as default user model
AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

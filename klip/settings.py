"""
Django settings for klip project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import pymysql
import os

pymysql.install_as_MySQLdb()


SOCIAL_AUTH_FACEBOOK_KEY = '267393197067693'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b0c96836f59b84ea22c3436ec72db669'  # App Secret

SOCIAL_AUTH_TWITTER_KEY = 'BGcPeS9n9kESEPcjaQyOMsqko'
SOCIAL_AUTH_TWITTER_SECRET = 'uSHt3Yqikw00UZRaJxz2oDK8o7sQ5XrBLwl98U1qqEbr8ODfKV'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '719505996632-bs0psdpiakak0bg35min6flo9a9jrep2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'JOEOGHLjncz05_OA7OEFr3zu'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i4s$i##ucjhgq244v3x739o+ti$espl-urrk48t_8k&@6tgk7='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['198.100.45.137', 'fujman.pythonanywhere.com', 'localhost']
CSRF_TRUSTED_ORIGINS = ['fujman.pythonanywhere.com', 'localhost']
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = True
# Application definition
SESSION_COOKIE_SECURE = False

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',  # <--
    'widget_tweaks',

    'users_app',
    'main_app',
    'paypal.standard.ipn'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'klip.urls'
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["%s/templates/" % PROJECT_PATH ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
        },
    },
]

## Added for auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'klip.EmailBackend.EmailBackend'
)

WSGI_APPLICATION = 'klip.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'OPTIONS': {
    #                'sql_mode': 'traditional',
    #            },
    #    'NAME': 'mydb',
    #    'USER': 'Fujman',
    #    'PASSWORD': '1q2w3e',
    #    'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    #    'PORT': '8889',
    #}
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'Fujman$default',
    #    'USER': 'Fujman',
    #    'PASSWORD': '1q2w3e4r5t',
    #    'HOST': 'Fujman.mysql.pythonanywhere-services.com',   # Or an IP Address that your DB is hosted on
    #    'OPTIONS': {
    #                        'sql_mode': 'traditional',
    #                    }
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'mydb',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'OPTIONS': {
                            'sql_mode': 'traditional',
                        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static/main_app")
STATIC_URL = '/static/main_app/'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


PAYPAL_RECEIVER_EMAIL = 'nanlicawork-facilitator@gmail.com'
PAYPAL_TEST = True

from .base import *

DEBUG = False

INSTALLED_APPS += [

]

if SITE_PREFIX:
    STATIC_URL = '/{}/static/'.format(SITE_PREFIX)
    MEDIA_URL = '/{}/media/'.format(SITE_PREFIX)
    SESSION_COOKIE_PATH = '/{}/'.format(SITE_PREFIX)
    LOGIN_REDIRECT_URL = '/{}/'.format(SITE_PREFIX)
    LOGIN_URL = '/{}/accounts/login/'.format(SITE_PREFIX)
    LOGOUT_URL = '/{}/accounts/logout/'.format(SITE_PREFIX)
    SESSION_COOKIE_NAME = '{}-session-id'.format(SITE_PREFIX)

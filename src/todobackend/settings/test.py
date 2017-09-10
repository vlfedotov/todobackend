import os

from .base import *


INSTALLED_APPS += ['django_nose']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
NOSE_ARGS = [
        '--verbosity=2',
        '--nologcapture',
        '--with-coverage',
        '--cover-package=todo',
        '--with-spec',
        '--spec-color',
        '--with-xunit',
        '--xunit-file={}/unittests.xml'.format(TEST_OUTPUT_DIR),
        '--cover-xml',
        '--cover-xml-file={}/coverage.xml'.format(TEST_OUTPUT_DIR),
    ]


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
            'USER': os.environ.get('MYSQL_USER', 'root'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'my-secret-pw'),
            'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
            'PORT': os.environ.get('MYSQL_PORT', '3306'),
        },
    }


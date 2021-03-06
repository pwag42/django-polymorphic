#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import django
from django.conf import settings
from django.core.management import execute_from_command_line


# Give feedback on used versions
sys.stderr.write('Using Python version {0} from {1}\n'.format(sys.version[:5], sys.executable))
sys.stderr.write('Using Django version {0} from {1}\n'.format(
    django.get_version(),
    dirname(abspath(django.__file__)))
)

if not settings.configured:
    settings.configure(
        DEBUG=False,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            },
            'secondary': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        TEST_RUNNER="django.test.runner.DiscoverRunner",
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.messages',
            'django.contrib.sites',
            'django.contrib.admin',
            'polymorphic',
        ),
        MIDDLEWARE_CLASSES=(),
        SITE_ID=3,
        TEMPLATES=[{
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": (),
                "OPTIONS": {
                    "loaders": (
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ),
                    "context_processors": (
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.request",
                        "django.template.context_processors.static",
                        "django.contrib.messages.context_processors.messages",
                        "django.contrib.auth.context_processors.auth",
                    ),
                },
            },
        ]
    )


DEFAULT_TEST_APPS = [
    'polymorphic',
]


def runtests():
    other_args = list(filter(lambda arg: arg.startswith('-'), sys.argv[1:]))
    test_apps = list(filter(lambda arg: not arg.startswith('-'), sys.argv[1:])) or DEFAULT_TEST_APPS
    argv = sys.argv[:1] + ['test', '--traceback'] + other_args + test_apps
    execute_from_command_line(argv)


if __name__ == '__main__':
    runtests()

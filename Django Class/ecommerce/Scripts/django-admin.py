#!c:\users\whoami\desktop\django class\ecommerce\scripts\python.exe
# When the django-admins.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admins.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admins instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admins.py is deprecated in favor of django-admins.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plants.settings')

if sys.argv[0] and sys.argv[0].find('django_test_manage.py'):
    import configurations
    configurations.setup()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plants.settings')
    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

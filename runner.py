# runner.py
import os
from django.core.management import execute_from_command_line

def main():
    # point to your project settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_management.settings")
    # start dev server (works on Windows; production can use gunicorn on Linux)
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])

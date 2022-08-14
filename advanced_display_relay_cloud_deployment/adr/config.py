"""
Configuration file for flask sample application
"""
import os

# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "you-will-never-guess")
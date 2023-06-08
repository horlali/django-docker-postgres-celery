import os

from dotenv import load_dotenv

from diagnosis.settings.base import *

# Load environment file
ENV_DIR = BASE_DIR.parent
load_dotenv(os.path.join(ENV_DIR, ".env.test"))

# Debug Mode
DEBUG = True

# Secret Keys
SECRET_KEY = os.getenv("SECRET_KEY")

# Allowed host
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True

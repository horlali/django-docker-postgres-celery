import os

from dotenv import load_dotenv

from diagnosis.settings.base import *

# Load environment file
ENV_DIR = BASE_DIR.parent
load_dotenv(os.path.join(ENV_DIR, ".env.prod"))

# Debug Mode
DEBUG = False

# Secret Keys
SECRET_KEY = os.getenv("SECRET_KEY")

# Allowed host
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

# CORS
# CORS
CORS_ALLOWED_ORIGINS = [
    os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000"),
]

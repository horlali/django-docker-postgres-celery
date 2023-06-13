import logging
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):
    help = "Create a superuser"

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                username="horlali",
                email=os.getenv("DEV_CONTACT"),
                password="password",
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully!"))
        except Exception as e:
            logger.error(f"Superuser already exists")

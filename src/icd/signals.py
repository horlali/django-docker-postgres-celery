import os

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from icd.models import CSVFile
from services.emails.messaging import send_mail
from services.utils.process_csv import add_category_data_to_db, add_diagnosis_data_to_db


@receiver(post_save, sender=CSVFile)
def file_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            recipient=instance.user.email,
            subject="ICD File Upload",
            content="File uploaded successfully",
        )

        file_path = instance.file.path
        if instance.type == "CATEGORY":
            add_category_data_to_db(os.path.join(settings.MEDIA_ROOT, file_path))

        if instance.type == "DIAGNOSIS":
            add_diagnosis_data_to_db(os.path.join(settings.MEDIA_ROOT, file_path))

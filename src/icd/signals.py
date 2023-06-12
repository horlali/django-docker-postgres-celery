from django.db.models.signals import post_save
from django.dispatch import receiver

from icd.models import File
from services.emails.messaging import send_mail


@receiver(post_save, sender=File)
def file_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            recipient=instance.user.email,
            subject="ICD File Upload",
            content="File uploaded successfully",
        )

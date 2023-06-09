from django.db import models


class IcdBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class ICD_Types(models.TextChoices):
    ICD_9 = "ICD_9", "ICD_9"
    ICD_10 = "ICD_10", "ICD_10"
    ICD_11 = "ICD_11", "ICD_11"


def file_upload_path(instance, filename: str) -> str:
    return f"files/{instance.user.username}/{filename}"

from time import time

from django.db import models
from drf_yasg import openapi


class IcdBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ICD_Types(models.TextChoices):
    ICD_9 = "ICD_9", "ICD_9"
    ICD_10 = "ICD_10", "ICD_10"
    ICD_11 = "ICD_11", "ICD_11"


class RecordType(models.TextChoices):
    CATEGORY = "Category", "Category"
    DIAGNOSIS = "Diagnosis", "Diagnosis"


def file_upload_path(instance, filename: str) -> str:
    return (
        f"files/{instance.user.username}/{instance.record_type}/{int(time())}_{filename}"
    )


file_upload_params = [
    openapi.Parameter(
        "file",
        openapi.IN_FORM,
        type=openapi.TYPE_FILE,
        description="CSV File to be uploaded",
    ),
    openapi.Parameter(
        "record_type",
        openapi.IN_FORM,
        type=openapi.TYPE_STRING,
        description="Record type of the file",
        enum=[RecordType.CATEGORY, RecordType.DIAGNOSIS],
    ),
]

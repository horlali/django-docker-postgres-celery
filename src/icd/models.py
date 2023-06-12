from django.contrib.auth.models import User
from django.db import models

from icd.extensions import FileType, ICD_Types, IcdBaseModel, file_upload_path


class Category(IcdBaseModel):
    category_code = models.CharField(max_length=25, unique=True)
    category_title = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["category_code"]

    def __str__(self):
        return self.category_title


class Diagnosis(IcdBaseModel):
    icd_type = models.CharField(
        max_length=12, choices=ICD_Types.choices, default=ICD_Types.ICD_10
    )
    category = models.ForeignKey(
        Category, related_name="diagnoses", on_delete=models.CASCADE
    )
    diagnosis_code = models.CharField(max_length=10, blank=True)
    abbreviated_desc = models.CharField(
        verbose_name="abbreviated description", max_length=2048
    )
    full_desc = models.TextField(verbose_name="full description", max_length=2048)

    @property
    def full_code(self):
        return f"{self.category.category_code}{self.diagnosis_code if self.diagnosis_code else ''}"  # noqa: E501

    class Meta:
        verbose_name_plural = "Diagnoses"
        ordering = ["id"]


class CSVFile(models.Model):
    file = models.FileField(upload_to=file_upload_path)
    type = models.CharField(max_length=12, choices=FileType.choices)
    user = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

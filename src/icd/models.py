from django.db import models


class ICD_Types(models.TextChoices):
    ICD_9 = "ICD_9", "ICD_9"
    ICD_10 = "ICD_10", "ICD_10"
    ICD_11 = "ICD_11", "ICD_11"


class IcdBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(IcdBaseModel):
    category_code = models.CharField(max_length=25, unique=True)
    category_title = models.CharField(max_length=1024)

    class Meta:
        ordering = ["category_code"]

    def __str__(self):
        return self.category_title


class Diagnosis(IcdBaseModel):
    icd_type = models.CharField(
        max_length=12,
        choices=ICD_Types.choices,
        default=ICD_Types.ICD_10,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    diagnosis_code = models.CharField(max_length=10, blank=True)
    abbreviated_desc = models.CharField(max_length=2048)
    full_desc = models.TextField(max_length=2048)

    @property
    def full_code(self):
        return f"{self.category.category_code}{self.diagnosis_code if self.diagnosis_code else ''}"  # noqa: E501

from django.urls import reverse
from rest_framework.test import APITestCase

from icd.models import Category, Diagnosis


class CategoryTestSetup(APITestCase):
    def setUp(self) -> None:
        self.category_1 = Category.objects.create(
            category_code="A01",
            category_title="Category 1",
        )
        self.category_2 = Category.objects.create(
            category_code="B01",
            category_title="Category 2",
        )
        self.category_list_create_url = reverse("category-list-create")
        self.category_detail_url = reverse(
            "category-detail",
            kwargs={"id": self.category_1.id},
        )


class DiagnosisTestSetup(APITestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(
            category_code="A01", category_title="Category 1"
        )
        self.diagnosis_1 = Diagnosis.objects.create(
            icd_type="ICD_9",
            category=self.category,
            diagnosis_code="A01",
            abbreviated_desc="Abbreviated Description 1",
            full_desc="Full Description 2",
        )
        self.diagnosis_2 = Diagnosis.objects.create(
            icd_type="ICD_10",
            category=self.category,
            diagnosis_code="B01",
            abbreviated_desc="Abbreviated Description 2",
            full_desc="Full Description 2",
        )
        self.diagnosis_3 = Diagnosis.objects.create(
            icd_type="ICD_11",
            category=self.category,
            diagnosis_code="C01",
            abbreviated_desc="Abbreviated Description 3",
            full_desc="Full Description 3",
        )
        self.diagnosis_list_create_url = reverse("diagnosis-list-create")
        self.diagnosis_detail_url = reverse(
            "diagnosis-detail",
            kwargs={"id": self.category.id},
        )

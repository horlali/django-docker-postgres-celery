import os
import shutil

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import DefaultStorage
from django.urls import reverse
from rest_framework.test import APITestCase

from icd.models import Category, Diagnosis

User = get_user_model()


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
            diagnosis_code="1",
            abbreviated_desc="Abbreviated Description 1",
            full_desc="Full Description 2",
        )
        self.diagnosis_2 = Diagnosis.objects.create(
            icd_type="ICD_10",
            category=self.category,
            diagnosis_code="1",
            abbreviated_desc="Abbreviated Description 2",
            full_desc="Full Description 2",
        )
        self.diagnosis_3 = Diagnosis.objects.create(
            icd_type="ICD_11",
            category=self.category,
            diagnosis_code="1",
            abbreviated_desc="Abbreviated Description 3",
            full_desc="Full Description 3",
        )
        self.diagnosis_list_create_url = reverse("diagnosis-list-create")
        self.diagnosis_detail_url = reverse(
            "diagnosis-detail",
            kwargs={"id": self.category.id},
        )


class FileTestSetup(APITestCase):
    def setUp(self) -> None:
        self.category_csv_data = (
            "A00,Cholera\n"
            "A01,Typhoid and paratyphoid fevers\n"
            "A010,Typhoid fever\n"
            "A011,Paratyphoid fever A\n"
            "A012,Paratyphoid fever B\n"
            "A013,Paratyphoid fever C\n"
            "A014,Paratyphoid fever, unspecified\n"
            "A02,Other salmonella infections\n"
        )
        self.category_csv_file = "test_category_data.csv"

        self.storage = DefaultStorage()
        self.storage.save(self.category_csv_file, ContentFile(self.category_csv_data))

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass",
        )

        self.file_upload_url = reverse("upload-csv")
        self.client.force_authenticate(user=self.user)

    def tearDown(self) -> None:
        self.storage.delete(self.category_csv_file)
        shutil.rmtree(
            os.path.join(settings.MEDIA_ROOT, "files/testuser"),
            ignore_errors=True,
        )
        return super().tearDown()

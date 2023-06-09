from django.urls import reverse
from rest_framework.test import APITestCase

from icd.models import Category


class CategoryTestSetup(APITestCase):
    def setUp(self) -> None:
        self.category1 = Category.objects.create(
            category_code="A01", category_title="Category 1"
        )
        self.category2 = Category.objects.create(
            category_code="B01", category_title="Category 2"
        )
        self.category_list_create_url = reverse("category-list-create")
        self.category_detail_url = reverse(
            "category-detail", kwargs={"id": self.category1.id}
        )

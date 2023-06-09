from rest_framework import status

from tests.test_icd.test_setup import CategoryTestSetup


class CategoryViewsTest(CategoryTestSetup):
    def test_list_categories(self):
        response = self.client.get(self.category_list_create_url, format="json")

        expected_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {"id": 1, "category_code": "A01", "category_title": "Category 1"},
                {"id": 2, "category_code": "B01", "category_title": "Category 2"},
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_data)

    def test_add_category(self):
        data = {"category_code": "C01", "category_title": "Category 3"}
        response = self.client.post(
            self.category_list_create_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        response = self.client.get(self.category_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        data = {"category_code": "Z01", "category_title": "Category 26"}
        response = self.client.patch(self.category_detail_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete(self.category_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
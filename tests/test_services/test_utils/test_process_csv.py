from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.test import TestCase

from icd.models import Category, Diagnosis
from services.utils.process_csv import add_category_data_to_db, add_diagnosis_data_to_db


class TestProcessCSVModule(TestCase):
    def setUp(self):
        self.category_csv_data = "A,Category A\nB,Category B\nC,Category C\n"
        self.category_csv_file = "test_category_data.csv"
        default_storage.save(self.category_csv_file, ContentFile(self.category_csv_data))

        self.diagnosis_csv_data = (
            "A,1001,A1001,abv. desc 1,full desc 1,cat.title 1\n"
            "B,2002,B2002,abv. desc 2,full desc 2,cat.title 2\n"
            "C,3003,C3003,abv. desc 3,full desc 3,cat.title 3\n"
            "D,4004,D4004,abv. desc 4,full desc 4,cat.title 4\n"
        )
        self.diagnosis_csv_file = "test_diagnosis_data.csv"
        default_storage.save(
            self.diagnosis_csv_file, ContentFile(self.diagnosis_csv_data)
        )

    def tearDown(self):
        default_storage.delete(self.category_csv_file)
        default_storage.delete(self.diagnosis_csv_file)

    def test_add_csv_data_to_db(self):
        add_category_data_to_db(default_storage.path(self.category_csv_file))

        categories = Category.objects.all()
        self.assertEqual(len(categories), 3)
        self.assertEqual(categories[0].category_code, "A")
        self.assertEqual(categories[0].category_title, "Category A")
        self.assertEqual(categories[1].category_code, "B")
        self.assertEqual(categories[1].category_title, "Category B")
        self.assertEqual(categories[2].category_code, "C")
        self.assertEqual(categories[2].category_title, "Category C")

    def test_add_diagnosis_data_to_db(self):
        cat_1 = Category.objects.create(category_code="A", category_title="Category A")
        cat_2 = Category.objects.create(category_code="B", category_title="Category B")
        cat_3 = Category.objects.create(category_code="C", category_title="Category C")

        add_diagnosis_data_to_db(default_storage.path(self.diagnosis_csv_file))
        diagnosis = Diagnosis.objects.all()

        self.assertEqual(len(diagnosis), 3)
        self.assertEqual(diagnosis[0].category, cat_1)
        self.assertEqual(diagnosis[0].diagnosis_code, 1001)
        self.assertEqual(diagnosis[0].full_code, "A1001")
        self.assertEqual(diagnosis[0].abbreviated_desc, "abv. desc 1")
        self.assertEqual(diagnosis[0].full_desc, "full desc 1")

        self.assertEqual(diagnosis[1].category, cat_2)
        self.assertEqual(diagnosis[1].diagnosis_code, 2002)
        self.assertEqual(diagnosis[1].full_code, "B2002")
        self.assertEqual(diagnosis[1].abbreviated_desc, "abv. desc 2")
        self.assertEqual(diagnosis[1].full_desc, "full desc 2")

        self.assertEqual(diagnosis[2].category, cat_3)
        self.assertEqual(diagnosis[2].diagnosis_code, 3003)
        self.assertEqual(diagnosis[2].full_code, "C3003")
        self.assertEqual(diagnosis[2].abbreviated_desc, "abv. desc 3")
        self.assertEqual(diagnosis[2].full_desc, "full desc 3")

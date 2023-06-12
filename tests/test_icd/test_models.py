from django.test import TestCase

from icd.models import Category, Diagnosis


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category_code="A01", category_title="Test Category")

    def test_category_data(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.category_code, "A01")
        self.assertEqual(category.category_title, "Test Category")

    def test_category_code_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("category_code").verbose_name
        self.assertEqual(field_label, "category code")

    def test_category_title_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("category_title").verbose_name
        self.assertEqual(field_label, "category title")

    def test_category_code_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field("category_code").max_length
        self.assertEqual(max_length, 25)

    def test_category_title_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field("category_title").max_length
        self.assertEqual(max_length, 1024)

    def test_category_code_unique(self):
        category = Category.objects.get(id=1)
        unique = category._meta.get_field("category_code").unique
        self.assertTrue(unique)

    def test_category_ordering(self):
        self.assertEqual(Category._meta.ordering, ["category_code"])

    def test_category_str(self):
        category = Category.objects.get(id=1)
        expected_str = category.category_title
        self.assertEqual(str(category), expected_str)


class DiagnosisModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            category_code="A01", category_title="Test Category"
        )
        Diagnosis.objects.create(
            icd_type="ICD-10",
            category=category,
            diagnosis_code="A001",
            abbreviated_desc="Test Diagnosis",
            full_desc="This is a test diagnosis",
        )

    def test_diagnosis_data(self):
        diagnosis = Diagnosis.objects.get(id=1)
        self.assertEqual(diagnosis.icd_type, "ICD-10")
        self.assertEqual(diagnosis.category.category_code, "A01")
        self.assertEqual(diagnosis.diagnosis_code, "A001")
        self.assertEqual(diagnosis.abbreviated_desc, "Test Diagnosis")
        self.assertEqual(diagnosis.full_desc, "This is a test diagnosis")

    def test_icd_type_label(self):
        diagnosis = Diagnosis.objects.get(id=1)
        field_label = diagnosis._meta.get_field("icd_type").verbose_name
        self.assertEqual(field_label, "icd type")

    def test_category_label(self):
        diagnosis = Diagnosis.objects.get(id=1)
        field_label = diagnosis._meta.get_field("category").verbose_name
        self.assertEqual(field_label, "category")

    def test_diagnosis_code_label(self):
        diagnosis = Diagnosis.objects.get(id=1)
        field_label = diagnosis._meta.get_field("diagnosis_code").verbose_name
        self.assertEqual(field_label, "diagnosis code")

    def test_abbreviated_desc_label(self):
        diagnosis = Diagnosis.objects.get(id=1)
        field_label = diagnosis._meta.get_field("abbreviated_desc").verbose_name
        self.assertEqual(field_label, "abbreviated description")

    def test_full_desc_label(self):
        diagnosis = Diagnosis.objects.get(id=1)
        field_label = diagnosis._meta.get_field("full_desc").verbose_name
        self.assertEqual(field_label, "full description")

    def test_icd_type_max_length(self):
        diagnosis = Diagnosis.objects.get(id=1)
        max_length = diagnosis._meta.get_field("icd_type").max_length
        self.assertEqual(max_length, 12)

    def test_diagnosis_code_max_length(self):
        diagnosis = Diagnosis.objects.get(id=1)
        max_length = diagnosis._meta.get_field("diagnosis_code").max_length
        self.assertEqual(max_length, 10)

    def test_abbreviated_desc_max_length(self):
        diagnosis = Diagnosis.objects.get(id=1)
        max_length = diagnosis._meta.get_field("abbreviated_desc").max_length
        self.assertEqual(max_length, 2048)

    def test_full_desc_max_length(self):
        diagnosis = Diagnosis.objects.get(id=1)
        max_length = diagnosis._meta.get_field("full_desc").max_length
        self.assertEqual(max_length, 2048)

    def test_full_code(self):
        diagnosis = Diagnosis.objects.get(id=1)
        expected_full_code = (
            f"{diagnosis.category.category_code}{diagnosis.diagnosis_code}"
        )
        self.assertEqual(diagnosis.full_code, expected_full_code)

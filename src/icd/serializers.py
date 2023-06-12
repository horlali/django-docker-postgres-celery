from rest_framework import serializers

from icd.extensions import FileType
from icd.models import Category, CSVFile, Diagnosis


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_code", "category_title"]


class DiagnosisSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Diagnosis
        fields = [
            "id",
            "icd_type",
            "category",
            "diagnosis_code",
            "abbreviated_desc",
            "full_desc",
            "full_code",
        ]


class FileSerializier(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    file_type = serializers.ChoiceField(choices=FileType.choices)

    class Meta:
        model = CSVFile
        fields = ["file", "file_type", "uploaded_at"]
        read_only_fields = ["user", "uploaded_at"]

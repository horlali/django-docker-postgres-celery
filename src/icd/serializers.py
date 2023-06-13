from rest_framework import serializers

from icd.extensions import FileType
from icd.models import Category, Diagnosis, ICDFile


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


class ICDFileSerializier(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    record_type = serializers.ChoiceField(choices=FileType.choices)

    class Meta:
        model = ICDFile
        fields = ["file", "record_type", "uploaded_at"]
        read_only_fields = ["user", "uploaded_at"]

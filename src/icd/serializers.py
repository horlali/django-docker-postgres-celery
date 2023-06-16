from rest_framework import serializers

from icd.extensions import RecordType
from icd.models import Category, Diagnosis, ICDFile


class CategorySerializer(serializers.ModelSerializer):
    category_code = serializers.CharField(max_length=25, required=True)
    category_title = serializers.CharField(max_length=1024, required=True)

    def validate_category_code(self, value):
        if Category.objects.filter(category_code__iexact=value).exists():
            raise serializers.ValidationError("Cateogory code already exists")
        return value

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
    record_type = serializers.ChoiceField(choices=RecordType.choices)

    class Meta:
        model = ICDFile
        fields = ["file", "record_type", "uploaded_at"]
        read_only_fields = ["user", "uploaded_at"]

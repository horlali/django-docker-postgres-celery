from rest_framework import serializers

from icd.models import Category, Diagnosis


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

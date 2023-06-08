from rest_framework import serializers

from icd.models import Category, Diagnosis


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_code", "category_title"]


class DiagnosisSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category_code = serializers.SerializerMethodField()
    # category_title = serializers.SerializerMethodField()

    # def get_category_code(self, obj):
    #     return str(obj.category.category_code)

    # def get_category_title(self, obj):
    #     return str(obj.category.category_title)

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
            # "category_code",
            # "category_title",
        ]

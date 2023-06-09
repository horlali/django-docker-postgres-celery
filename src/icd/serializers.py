from rest_framework import serializers

from icd.models import Category, Diagnosis, File
from services.emails.messaging import send_mail


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


class FilesSerializier(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = File
        fields = ["file", "uploaded_at"]

    def create(self, validated_data):
        file_obj = super().create(validated_data)

        # send email after file is uploaded successfully
        send_mail(
            receipient=file_obj.user.email,
            subject="ICD File Upload",
            content="File uploaded successfully",
        )

        return file_obj

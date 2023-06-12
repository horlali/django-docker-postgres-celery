from django.urls import path

from icd.views import (
    CategoryDetailView,
    CategoryListCreateView,
    DiagnosisDetailView,
    DiagnosisListCreateView,
    UploadICDFileView,
)

urlpatterns = [
    path("category", CategoryListCreateView.as_view(), name="category-list-create"),
    path("category/<int:id>", CategoryDetailView.as_view(), name="category-detail"),
    path("diagnosis", DiagnosisListCreateView.as_view(), name="diagnosis-list-create"),
    path("diagnosis/<int:id>", DiagnosisDetailView.as_view(), name="diagnosis-detail"),
    path("upload-csv", UploadICDFileView.as_view(), name="upload-csv"),
]

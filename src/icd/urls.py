from django.urls import path

from icd.views import (
    CategoryDetailView,
    CategoryListView,
    DiagnosisDetailView,
    DiagnosisListView,
    UploadICDFileView,
)

urlpatterns = [
    path("category", CategoryListView.as_view(), name="category-list-create"),
    path("category/<int:id>", CategoryDetailView.as_view(), name="category-detail"),
    path("diagnosis", DiagnosisListView.as_view(), name="diagnosis-list-create"),
    path("diagnosis/<int:id>", DiagnosisDetailView.as_view(), name="diagnosis-detail"),
    path("upload", UploadICDFileView.as_view(), name="upload"),
]

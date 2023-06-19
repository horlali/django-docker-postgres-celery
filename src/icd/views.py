from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from icd.extensions import file_upload_params
from icd.models import Category, Diagnosis
from icd.paginations import CustomPagination
from icd.serializers import CategorySerializer, DiagnosisSerializer, ICDFileSerializier


@method_decorator(cache_page(10 * 60), name="dispatch")
class CategoryListCreateView(ListCreateAPIView):
    """List all categories or create a new category."""

    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPagination


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a category instance."""

    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"


@method_decorator(cache_page(10 * 60), name="dispatch")
class DiagnosisListCreateView(ListCreateAPIView):
    """List all diagnoses or create a new diagnosis."""

    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    pagination_class = CustomPagination


class DiagnosisDetailView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a diagnosis instance."""

    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    lookup_field = "id"


class ICDFileUploadView(CreateAPIView):
    """Upload an ICD file."""

    permission_classes = [IsAuthenticated]
    serializer_class = ICDFileSerializier
    parser_classes = (MultiPartParser, FileUploadParser)

    @swagger_auto_schema(manual_parameters=file_upload_params)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

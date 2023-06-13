from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from icd.extensions import file_upload_params
from icd.models import Category, Diagnosis, ICDFile
from icd.paginations import CustomPagination
from icd.serializers import CategorySerializer, DiagnosisSerializer, ICDFileSerializier


class CategoryListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPagination


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"


class DiagnosisListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    pagination_class = CustomPagination


class DiagnosisDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    lookup_field = "id"


class ICDFileUploadView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FileUploadParser)
    serializer_class = ICDFileSerializier

    def get_queryset(self):
        return ICDFile.objects.filter(user=self.request.user)

    @swagger_auto_schema(manual_parameters=file_upload_params)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

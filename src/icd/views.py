from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from icd.models import Category, Diagnosis
from icd.paginations import CustomPagination
from icd.serializers import CategorySerializer, DiagnosisSerializer


class CategoryListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Category.objects.all()
    pagination_class = CustomPagination


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"


class DiagnosisListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    pagination_class = CustomPagination


class DiagnosisDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()
    lookup_field = "id"


class UploadICDFileView(APIView):
    permission_classes = [IsAuthenticated | AllowAny]
    # serializer_class = DiagnosisSerializer

    def post(self, request, *args, **kwargs):
        return Response({"message": "Got some data!", "data": request.data})

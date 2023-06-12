from django.contrib import admin

from icd.models import Category, CSVFile, Diagnosis

admin.site.register(Category)
admin.site.register(Diagnosis)
admin.site.register(CSVFile)

from django.contrib import admin

from icd.models import Category, Diagnosis, ICDFile

admin.site.register(Category)
admin.site.register(Diagnosis)
admin.site.register(ICDFile)

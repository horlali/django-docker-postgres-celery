from django.contrib import admin

from icd.models import Category, Diagnosis, File

admin.site.register(Category)
admin.site.register(Diagnosis)
admin.site.register(File)

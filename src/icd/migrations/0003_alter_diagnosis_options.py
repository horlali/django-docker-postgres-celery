# Generated by Django 4.2.2 on 2023-06-10 01:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("icd", "0002_rename_files_file_alter_diagnosis_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diagnosis",
            options={"ordering": ["id"], "verbose_name_plural": "Diagnoses"},
        ),
    ]
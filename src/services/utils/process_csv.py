from os import PathLike

import pandas as pd
from celery import shared_task
from django.db import transaction

from icd.models import Category, Diagnosis

CATEGORY_COLUMNS = ["category_code", "category_title"]
DIAGNOSIS_COLUMNS = [
    "category_code",
    "diagnosis_code",
    "full_code",
    "abbreviated_description",
    "full_description",
    "category_title",
]


@shared_task()
def add_category_data_to_db(csv_file: PathLike) -> None:
    """Adds category data to the database from a CSV file.

    Args:
        csv_file (PathLike): The path to the CSV file containing the category data.

    Returns:
        None
    """
    category_df = pd.read_csv(csv_file, names=CATEGORY_COLUMNS)
    category_df.dropna(subset="category_code", inplace=True)
    category_df = category_df.drop_duplicates(subset=["category_code"], keep="first")

    dataset = [
        Category(category_code=row.category_code, category_title=row.category_title)
        for row in category_df.itertuples()
    ]

    with transaction.atomic():
        Category.objects.bulk_create(dataset, ignore_conflicts=True, batch_size=2000)

    return "finished"


@shared_task()
def add_diagnosis_data_to_db(csv_file: PathLike) -> None:
    """Adds Diagnosis data to the database from a CSV file.

    Args:
        csv_file (PathLike): The path to the CSV file containing the category data.

    Returns:
        None
    """

    diagnosis_df = pd.read_csv(csv_file, names=DIAGNOSIS_COLUMNS)
    diagnosis_df.dropna(subset="full_code", inplace=True)
    diagnosis_df = diagnosis_df.drop_duplicates(subset=["full_code"], keep="first")

    dataset = list()

    for _index, row in diagnosis_df.iterrows():
        try:
            category_obj = Category.objects.get(category_code=row["category_code"])

            dataset.append(
                Diagnosis(
                    category=category_obj,
                    diagnosis_code=row["diagnosis_code"],
                    abbreviated_desc=row["abbreviated_description"],
                    full_desc=row["full_description"],
                )
            )
        except Category.DoesNotExist:
            continue

    with transaction.atomic():
        Diagnosis.objects.bulk_create(dataset, ignore_conflicts=True, batch_size=7000)

    return "finished"

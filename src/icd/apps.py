from django.apps import AppConfig


class IcdConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "icd"

    def ready(self) -> None:
        import icd.signals  # noqa: F401

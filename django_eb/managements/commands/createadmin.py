from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from django_eb import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.DEFAULT_ADMIN_NAME).exists():
            User.objects.create_superuser(
                settings.DEFAULT_ADMIN_NAME,
                settings.DEFAULT_ADMIN_EMAIL,
                settings.DEFAULT_ADMIN_PASSWORD,
            )

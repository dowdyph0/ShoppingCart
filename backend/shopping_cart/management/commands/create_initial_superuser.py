from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = os.getenv("DJANGO_DEFAULT_ADMIN_USERNAME", "admin")
            password = os.getenv("DJANGO_DEFAULT_ADMIN_PASSWORD", "admin1234")
            admin = User.objects.create_superuser(username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            raise CommandError('Admin accounts can only be initialized if no Users exist')
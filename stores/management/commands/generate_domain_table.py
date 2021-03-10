"""
 Gets domains of all URLs.
"""

import csv
from django.core.management.base import BaseCommand, CommandError
from stores import utils
from ratelimit import limits, RateLimitException

class Command(BaseCommand):
    help = ("Get domains of all URLs")

    def handle(self, *args, **options):
        from stores.models import Store, Domain

        objects = Store.objects.filter(url__contains="http", domain__isnull=True)

        for object in objects:
            try:
                new_domain, created = Domain.objects.get_or_create(name=object.domain_only())
                object.domain=new_domain
                object.save()
                self.stdout.write(f"Saved: {new_domain}")
            except Exception as e:
                self.stdout.write(f"Errored: {e}")

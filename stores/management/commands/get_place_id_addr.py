"""
 Gets Place IDs of all unknown places.
"""

import csv
from django.core.management.base import BaseCommand, CommandError
from stores import utils
from ratelimit import limits, RateLimitException

class Command(BaseCommand):
    help = ("Get Place IDs of all unknown places")

    @limits(calls=99, period=60)
    def handle(self, *args, **options):
        from stores.models import Store

        objects = Store.objects.filter(place_id__isnull=True)
        for object in objects:
            try:
                result = utils.get_places_id(object)
                object.place_id=result
                object.save()
                self.stdout.write(f"Saved: {object}")
            except Exception as e:
                self.stdout.write(f"Errored: {e}")

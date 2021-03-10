"""
 Gets Website URL of all known places.
"""

import csv
from django.core.management.base import BaseCommand, CommandError
from stores import utils
from ratelimit import limits, RateLimitException

class Command(BaseCommand):
    help = ("Get Website URL of all known places")

    @limits(calls=99, period=60)
    def handle(self, *args, **options):
        from stores.models import Store

        objects = Store.objects.filter(place_id__isnull=False, url__exact="")
        for object in objects:
            try:
                result = utils.get_place_details(object.place_id)
                object.business_status = result.get("business_status")
                object.formatted_address = result.get("formatted_address")
                object.icon = result.get("icon")
                try:
                    object.latitude = result.get("geometry").get("location").get("lat")
                    object.longitude = result.get("geometry").get("location").get("lng")
                except Exception:
                    pass
                object.listed_name = result.get("name")
                if not object.url:
                    object.url = result.get("website")
                object.save()
                self.stdout.write(f"Saved: {object} {object.url}")

            except Exception as e:
                self.stdout.write(f"Errored: {e}")

"""
 Checks validity of an email
"""

from django.core.management.base import BaseCommand, CommandError
import logging
import requests
from locations import secrets
from crm.models import leads

logger = logging.getLogger(__file__)


class Command(BaseCommand):
    help = "Checks validity of an email"

    def handle(self, *args, **options):
        queryset = leads.objects.filter(stage_id__isnull=True)

        for query in queryset:
            try:
                data = {
                    'api': secrets.DEBOUNCE_API_KEY,
                    'email': query.email
                }
                r = requests.get("https://api.debounce.io/v1/", params=data)
                debounce_data = r.json()
                debounce_data = debounce_data.get("debounce", {})
                logger.info(debounce_data)

                if debounce_data.get("reason", "") in ["Deliverable", "Valid"]:
                    query.stage_id = 2  # Safe to Send
                elif debounce_data.get("reason", "") in ["Accept-All", "Unknown"]:
                    query.stage_id = 1  # Risky
                elif debounce_data.get("reason", "") in ["Syntax"]:
                    query.stage_id = 3  # Unknown
                elif debounce_data.get("result", "") in ["Invalid", "Disposable", "Spam Trap", "Role"]:
                    query.stage_id = 4  # Unsafe

                query.save()
            except Exception as e:
                logger.warning(e)

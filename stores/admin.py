from django.contrib import admin

# Register your models here.
from .models import Store, Domain
from . import utils

admin.site.register(Domain)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=('name', 'place_id', 'listed_name', 'url')
    actions = ['query_place_id', 'query_place_id_phone', "query_place_details"]

    def query_place_id(self, request, queryset):
        for query in queryset[:99]:
            try:
                result = utils.get_places_id(query)
                query.place_id=result
                query.save()
            except Exception as e:
                print(e)
    query_place_id.short_description = "Get Place ID by Address"

    def query_place_id_phone(self, request, queryset):
        for query in queryset[:99]:
            try:
                result = utils.get_places_id_phone(query)
                if not result:
                    raise Exception("No or Multiple Results Found")
                query.place_id = result
                query.save()
                print(f"Saved: {query}")
            except Exception as e:
                print(e)
    query_place_id_phone.short_description = "Get Place ID by Phone"

    def query_place_details(self, request, queryset):
        for query in queryset[:99]:
            try:
                result = utils.get_place_details(query.place_id)
                if not result:
                    raise Exception("No or Multiple Results Found")
                query.business_status = result.get("business_status")
                query.formatted_address = result.get("formatted_address")
                query.icon = result.get("icon")
                try:
                    query.latitude = result.get("geometry").get("location").get("lat")
                    query.longitude = result.get("geometry").get("location").get("lng")
                except Exception:
                    pass
                query.listed_name = result.get("name")
                if not query.url:
                    query.url = result.get("website")
                query.save()
            except Exception as e:
                print(e)
    query_place_details.short_description = "Get Place Details"

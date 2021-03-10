import googlemaps
import requests
from locations import secrets
import logging

logger = logging.getLogger(__file__)

PLACES_API_KEY=secrets.PLACES_API_KEY

def get_places_id(object):
    gmaps = googlemaps.Client(PLACES_API_KEY)
    query = f"{object.name} {object.address_line_1} {object.address_line_2} {object.city} {object.state} {object.postcode}"
    place_search_result = gmaps.find_place(query, "textquery", fields=["place_id"])
    candidates = place_search_result.get("candidates", [])
    if len(candidates) == 1:
        return candidates[0].get("place_id")

def get_places_id_phone(object):
    gmaps = googlemaps.Client(PLACES_API_KEY)
    query = f"+1{object.phone}"
    place_search_result = gmaps.find_place(query, "phonenumber", fields=["place_id"])
    candidates = place_search_result.get("candidates", [])
    if len(candidates) == 1:
        return candidates[0].get("place_id")

def get_place_details(places_id):
    gmaps = googlemaps.Client(key=PLACES_API_KEY)
    place_details = gmaps.place(places_id, fields=["business_status", "icon", "geometry/location", "name", "formatted_address", "website"])
    result = place_details.get("result", {})
    return result

def get_domain_only(url):
    from tldextract import extract
    tsd, td, tsu = extract(url)  # prints abc, hostname, com
    return td + '.' + tsu  # will prints as hostname.com

def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

def queryset_to_unique_domain_list(queryset):
    domain_list=[]
    for query in queryset:
        try:
            domain = get_domain_only(query.url)
            domain_list += [domain]
        except:
            pass
    return unique(domain_list)

def hunterio_lookup(domain):
    from crm.models import leads
    data = {
        'domain': domain.name,
        'api_key': secrets.HUNTERIO_API_KEY,
        'limit': 100,
        'type': 'personal',
    }
    r = requests.get("https://api.hunter.io/v2/domain-search", params=data)
    hunter_data = r.json()
    hunter_data = hunter_data.get("data")
    emails = hunter_data.get("emails", [])
    logger.info(emails)
    for email in emails:
        lead, created = leads.objects.update_or_create(
            email=email.get("value"),
            defaults={
                'firstname': email.get('first_name', ''),
                'lastname': email.get('last_name', ''),
                'position': email.get('position', ''),
                'company': domain.name,
                'points': len(email.get('sources', []))
            }
        )
    return len(emails)
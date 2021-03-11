# Documentation for Use of the Limitless Interactive Flywheel Techstack
The LIFT is a custom application built in Django 3.1 intended to convert a list of street addresses into a list of email addresses.

0. **Create secrets.py next to settings.py**
    - DATABASE_PASS=
    - DATABASE_USER=
    - DATABASE_HOST=
    - PLACES_API_KEY=
    - DEVBOX_IP=
    - HUNTERIO_API_KEY=
    - DEBOUNCE_API_KEY=

1. **Place the street addresses in a .csv file with the following column headers:**

    - name,address_line_1,address_line_2,city,state,postcode,phone,url

2. **Import the list into the django model.**

    - python manage.py importcsv --model=stores.store --delimiter="," MyLeadFile.csv

3. **Query Google Places API for the List of Place_IDs by Address**

    - python manage.py get_place_id_addr

4. **Query Google Places API for the List of Place_IDs by Phone Number**

    - python manage.py get_place_id_phone

5. **Query Google Places API for the Detailed Information of each Place**

    - python manage.py get_place_details

6. **Generate the Django Domains table.**

    - python manage.py generate_domain_table

7. **Find Emails via Hunter.io**
    - From the Domain Admin screen, select relevant domains and use dropdown for Hunter.io
 
8. **Debounce.io Lead Deliverability Report**
    - From the Leads Admin screen, select relevant leads and use dropdown for Debounce.io
    - This integration works with trhr/django-mautic

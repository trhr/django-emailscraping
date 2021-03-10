# Documentation for Use of the Limitless Interactive Flywheel Techstack
The LIFT is a custom application built in Django 3.1 intended to convert a list of street addresses into a list of email addresses.

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

7. **Export to CSV.**

    - python manage.py model2csv stores.Store MyListExport.csv

8. **Generate Unique Domain List in LibreOffice.**

    - Select the entire Range to find distinct rows in ( e.g. "A1:B99" ),
    - Choose the menu "Data : More Filters : Standard Filter...",
    - In the dialog box that appears, in the first row of the Filter Criteria, set the Field Name to "- none -",
    - Expand the Options by clicking on the small triangle, 
    - Check the checkbox "No duplications",
    - Check the checkbox "Copy results to:" and enter a full Target CellAddress into the textbox ( e.g. "Sheet1.D1" ),
    - Uncheck the checkbox "Keep filter criteria",
    - Check the checkbox "Range contains column labels",
    - Click OK.

9. **Bulk Import Applicable Domains into Hunter.IO**

    - Bulks -> Domain Search -> Copy & Paste domains from Excel
    - Import these Leads to a Hunter.IO Lead List

10. **Validate Email Addresses with debounce**

    - Export leads from Hunter.IO to CSV
    - Import CSV into debounce.io


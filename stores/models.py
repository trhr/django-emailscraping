from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True)
    address_line_1 = models.CharField(max_length=127, blank=True, null=True)
    address_line_2 = models.CharField(max_length=127, blank=True, null=True)
    city = models.CharField(max_length=127, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    postcode = models.CharField(max_length=9, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    business_status=models.CharField(max_length=32, blank=True, null=True)
    icon=models.URLField(blank=True,null=True)
    latitude=models.CharField(max_length=32,blank=True,null=True)
    longitude=models.CharField(max_length=32,blank=True,null=True)
    listed_name=models.CharField(max_length=127, blank=True, null=True)
    place_id=models.CharField(max_length=127, blank=True, null=True)
    formatted_address=models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    domain = models.ForeignKey('Domain', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        if self.listed_name:
            return self.listed_name
        else:
            return self.name

    def domain_only(self):
        from tldextract import extract
        try:
            tsd, td, tsu = extract(self.url)  # prints abc, hostname, com
            if tsu:
                return td + '.' + tsu  # will prints as hostname.com
        except Exception as e:
            return None

class Domain(models.Model):
    name = models.CharField(max_length=63, primary_key=True)

    def __str__(self):
        return self.name

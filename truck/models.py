from django.db import models


class Truck(models.Model):
    """Truck model based on csv file"""
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255, null=True, blank=True)
    cnn = models.CharField(max_length=255, null=True, blank=True)
    location_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    block_lot = models.CharField(max_length=255, null=True, blank=True)
    block = models.CharField(max_length=255, null=True, blank=True)
    lot = models.CharField(max_length=255, null=True, blank=True)
    permit = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    food_items = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=255, null=True, blank=True)
    days_hours = models.CharField(max_length=255, null=True, blank=True)
    noi_sent = models.CharField(max_length=255, null=True, blank=True)
    approved = models.DateField(null=True, blank=True)
    received = models.CharField(max_length=255, null=True, blank=True)
    prior_permit = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    fire_prevention_districts = models.IntegerField(null=True, blank=True)
    police_districts = models.IntegerField(null=True, blank=True)
    supervisor_districts = models.IntegerField(null=True, blank=True)
    zip_codes = models.CharField(max_length=255, null=True, blank=True)
    neighborhoods_old = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.applicant

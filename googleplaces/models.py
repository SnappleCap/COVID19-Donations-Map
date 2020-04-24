from djgeojson.fields import PointField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=256)
	address = models.CharField(max_length=100)
	phone_number = PhoneNumberField(required=True)
	geom = PointField()
	website = models.CharField(max_length=100)
	notes = models.CharField(max_length=256)

	@property
	def popupContent(self):
		return '<h5><strong>{}</strong></h5><h6>{}</h6><h6><a href="tel:{}">{}</a></h6><h6><a href="{}" target="_blank">{}</a></h6>'.format(self.address, self.notes, self.phone_number, self.phone_number, self.website, self.website)

	def __unicode__(self):
		return self.name
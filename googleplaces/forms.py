from django import forms
from .models import Location as LocationModel
from leaflet.forms.widgets import LeafletWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LocationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(LocationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout.append(Submit('Add To Map', 'Add To Map', css_class='btn-success'))
	class Meta:
		model = LocationModel
		fields = ('name', 'phone_number', 'address', 'website', 'notes')
		labels = {
            'phone_number': 'Phone Number (e.g. 716-555-5555)',
            'website': 'Website (e.g. https://www.google.com)',
            'notes': 'Donation Requests'
        }
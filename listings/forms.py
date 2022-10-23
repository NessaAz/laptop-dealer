from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm

from .models import *

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'name',
            'description',
            'brand',
            'used',
            'price',
            'image',
        ]
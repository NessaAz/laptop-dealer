from django.shortcuts import render

from .models import *

def listings(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }

    return render(request, 'listings.html',context)
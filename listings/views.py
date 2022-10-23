from django.shortcuts import render

from .models import *

def listings(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html',context)


def listing(request, id)    :

    listing = Listing.objects.get(id=id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)
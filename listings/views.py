from django.shortcuts import render, redirect

from .models import *
from .forms import *

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




def create_listing(request):

    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'listings/create_listing.html', context)



def update_listing(request, id):

    listing = Listing.objects.get(id=id)    #query from db
    form = ListingForm(instance=listing)#populate the form by passing an instance and equate to listing

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'listings/update_listing.html', context)




def delete_listing(request, id):

    listing = Listing.objects.get(id=id)
    listing.delete()

    return redirect('/')
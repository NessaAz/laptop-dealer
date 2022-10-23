from django.urls import path

from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('create-listing/', views.create_listing, name='create_listing'),  
    path('listing/<id>/', views.listing, name='listing'),

]
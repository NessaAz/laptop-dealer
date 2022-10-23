from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('create-listing/', views.create_listing, name='create_listing'),  
    path('update-listing/<id>/', views.update_listing, name='updeate_listing'),  
    path('delete-listing/<id>/', views.delete_listing, name='delete_listing'),  
    path('listing/<id>/', views.listing, name='listing'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
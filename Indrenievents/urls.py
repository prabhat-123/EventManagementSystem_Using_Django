from django.contrib import admin
from django.urls import path, include


from . import views
app_name= 'Indrenievents'
urlpatterns=[
    path('{showallevents.Eventnameid}/<int:pk>/',views.eventdetailspage, name= 'eventdetails')

]
from django.urls import path
from . import views

urlpatterns = [
    path('',                views.index,           name='index'),
    path('fishing/',        views.fishing,         name='fishing'),
    path('excursions/',     views.excursions,       name='excursions'),
    path('gallery/',        views.gallery,         name='gallery'),
    path('booking/',        views.booking,         name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
]

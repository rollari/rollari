from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ('name', 'experience', 'preferred_date', 'adults', 'email', 'status', 'created_at')
    list_filter   = ('status', 'experience', 'preferred_date')
    search_fields = ('name', 'email', 'phone')
    ordering      = ('-created_at',)
    list_editable = ('status',)

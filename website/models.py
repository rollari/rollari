from django.db import models


class Booking(models.Model):
    EXPERIENCE_CHOICES = [
        ('deep_sea',       'Deep Sea Big Game Fishing'),
        ('night_fishing',  'Traditional Night Fishing'),
        ('sport_trolling', 'Sport Trolling'),
        ('whale_shark',    'Whale Shark Safari'),
        ('manta_ray',      'Manta Ray Encounter'),
        ('dolphin_cruise', 'Dolphin Sunset Cruise'),
        ('sandbank',       'Sandbank Picnic'),
        ('island_hopping', 'Island Hopping Adventure'),
        ('snorkeling',     'Snorkeling Expedition'),
        ('ultimate',       'Ultimate Ocean Expedition (Signature)'),
        ('custom',         'Custom / Multiple Experiences'),
    ]

    STATUS_CHOICES = [
        ('pending',    'Pending'),
        ('confirmed',  'Confirmed'),
        ('cancelled',  'Cancelled'),
    ]

    name            = models.CharField(max_length=200, verbose_name='Full Name')
    email           = models.EmailField(verbose_name='Email Address')
    phone           = models.CharField(max_length=30, verbose_name='Phone Number')
    whatsapp        = models.CharField(max_length=30, blank=True, verbose_name='WhatsApp Number')
    nationality     = models.CharField(max_length=100, blank=True, verbose_name='Nationality')
    adults          = models.PositiveIntegerField(default=2, verbose_name='Number of Adults')
    children        = models.PositiveIntegerField(default=0, verbose_name='Number of Children')
    experience      = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, verbose_name='Experience')
    preferred_date  = models.DateField(verbose_name='Preferred Date')
    flexible_dates  = models.BooleanField(default=False, verbose_name='Flexible with Dates')
    special_requests = models.TextField(blank=True, verbose_name='Special Requests')
    source          = models.CharField(max_length=100, blank=True, verbose_name='How did you hear about us?')
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"{self.name} — {self.get_experience_display()} — {self.preferred_date}"

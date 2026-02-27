from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone', 'whatsapp', 'nationality',
            'adults', 'children', 'experience', 'preferred_date',
            'flexible_dates', 'special_requests', 'source',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+1 234 567 8900',
                'class': 'form-input',
            }),
            'whatsapp': forms.TextInput(attrs={
                'placeholder': '+1 234 567 8900 (if different)',
                'class': 'form-input',
            }),
            'nationality': forms.TextInput(attrs={
                'placeholder': 'e.g. British, American',
                'class': 'form-input',
            }),
            'adults': forms.NumberInput(attrs={
                'min': 1, 'max': 20,
                'class': 'form-input',
            }),
            'children': forms.NumberInput(attrs={
                'min': 0, 'max': 10,
                'class': 'form-input',
            }),
            'experience': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
            'preferred_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
            }),
            'flexible_dates': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
            'special_requests': forms.Textarea(attrs={
                'placeholder': 'Dietary requirements, accessibility needs, special occasions, custom itinerary wishes…',
                'class': 'form-input form-textarea',
                'rows': 4,
            }),
            'source': forms.Select(attrs={
                'class': 'form-input form-select',
            }, choices=[
                ('', 'Please select…'),
                ('google', 'Google Search'),
                ('instagram', 'Instagram'),
                ('facebook', 'Facebook'),
                ('tiktok', 'TikTok'),
                ('friend', 'Friend / Family Recommendation'),
                ('hotel', 'Hotel / Resort Recommendation'),
                ('tripadvisor', 'TripAdvisor'),
                ('other', 'Other'),
            ]),
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'form-input',
            }),
        }

    def clean_preferred_date(self):
        from datetime import date
        d = self.cleaned_data.get('preferred_date')
        if d and d < date.today():
            raise forms.ValidationError("Please choose a future date.")
        return d

    def clean_adults(self):
        n = self.cleaned_data.get('adults')
        if n and n < 1:
            raise forms.ValidationError("At least 1 adult required.")
        return n

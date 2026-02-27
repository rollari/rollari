from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm


def index(request):
    return render(request, 'website/index.html')


def fishing(request):
    return render(request, 'website/fishing.html')


def excursions(request):
    return render(request, 'website/excursions.html')


def gallery(request):
    return render(request, 'website/gallery.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_obj = form.save()
            request.session['booking_id'] = booking_obj.id
            request.session['booking_name'] = booking_obj.name
            request.session['booking_experience'] = booking_obj.get_experience_display()
            return redirect('booking_success')
    else:
        experience = request.GET.get('experience', '')
        initial = {'experience': experience} if experience else {}
        form = BookingForm(initial=initial)

    return render(request, 'website/booking.html', {'form': form})


def booking_success(request):
    name = request.session.pop('booking_name', 'Guest')
    experience = request.session.pop('booking_experience', 'your experience')
    return render(request, 'website/booking_success.html', {
        'name': name,
        'experience': experience,
    })

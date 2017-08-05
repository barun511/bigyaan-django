from django.shortcuts import render
from .models import Marker
from .models import Testimonial

# Create your views here.
def index(requests):
    return render(requests, 'website/index.html', {})

def aboutus(requests):
    return render(requests, 'website/aboutus.html', {})

def studentsworkshops(requests):    
    return render(requests, 'website/studentsworkshops.html', {})

def ourstory(requests):
    markers = Marker.objects.all()
    testimonials = Testimonial.objects.order_by('order_number')
    return render(requests, 'website/ourstories.html', {'markers': markers, 'testimonials': testimonials})


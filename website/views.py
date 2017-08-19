from django.shortcuts import render
from .models import Marker
from .models import Testimonial
from photologue.models import Gallery

# Create your views here.
def index(requests):
    return render(requests, 'website/index.html', {})

def aboutus(requests):
    return render(requests, 'website/aboutus.html', {})

def workshops(requests):    
    return render(requests, 'website/workshops.html', {})

def gallery(requests):
    galleries = Gallery.objects.all()
    return render(requests, 'website/gallery.html', {'galleries' : galleries})

def ourstory(requests):
    markers = Marker.objects.all()
    testimonials = Testimonial.objects.order_by('order_number')
    return render(requests, 'website/ourstories.html', {'markers': markers, 'testimonials': testimonials})


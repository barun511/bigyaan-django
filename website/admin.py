from django.contrib import admin
from .models import Image
from .models import Marker
from .models import Testimonial

# Register your models here.
admin.site.register(Image)
admin.site.register(Marker)
admin.site.register(Testimonial)

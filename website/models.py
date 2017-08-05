from django.db import models
from django.utils import timezone

    
class Image(models.Model):
    album = models.TextField()
    image_name = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)

class Marker(models.Model):
    def __str__(self):
        return self.title + ' ( ' + str(self.latitude) + ', ' + str(self.longitude) + ' )'
    latitude = models.FloatField()
    longitude = models.FloatField()
    title = models.TextField()

class Testimonial(models.Model):
    def __str__(self):
        return self.name
    order_number = models.IntegerField()
    text = models.TextField()
    name = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

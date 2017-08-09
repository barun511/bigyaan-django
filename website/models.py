from django.db import models
from django.utils import timezone

    

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

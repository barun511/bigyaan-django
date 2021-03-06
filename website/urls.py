from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^aboutus$', views.aboutus, name="aboutus"),
    url(r'^ourstory$', views.ourstory, name="ourstory"),
    url(r'^workshops$', views.workshops, name="workshops"),
 #   url(r'^gallery/?$', views.gallery, name="gallery"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

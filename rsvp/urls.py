from django.conf.urls import url
from .views import RSVP


urlpatterns = [
    url(r'^rsvp/$', RSVP.as_view(), name='rsvp'),
]

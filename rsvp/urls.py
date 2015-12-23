from django.conf.urls import url
from rsvp.views import RSVPComplete
from .views import RSVP


urlpatterns = [
    url(r'^$', RSVP.as_view(), name='rsvp'),
    url(r'^rsvp/thank-you$', RSVPComplete.as_view(), name='thank-you'),
]

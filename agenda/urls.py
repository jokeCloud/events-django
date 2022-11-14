from django.urls import path

from agenda.views import list_events, show_event

urlpatterns = [
    path('', list_events),
    path('event', show_event),
]

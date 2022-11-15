from django.urls import path

from agenda.views import enjoy_event, list_events, show_event

urlpatterns = [
    path('', list_events, name='list-events'),
    path('event/<int:id>/', show_event, name='show-event'),
    path('enjoy/', enjoy_event, name='enjoy_event')
]

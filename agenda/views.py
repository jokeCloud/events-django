from datetime import date

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from agenda.models import Event

# from django.template import loader


def list_events(request):
    events = Event.objects.exclude(
        date__lt=date.today()
    )
    return render(request, 'agenda/list_events.html', context={'events': events})  # noqa
    """
    events = Event.objects.all()
    return render(
        request=request,
        context={'events': events},
        template_name='agenda/list_events.html'
    )  # noqa
    """


def show_event(request, id):
    event = get_object_or_404(Event, id=id)
    event = Event.objects.get(id=id)
    return render(
        request=request,
        context={'event': event},
        template_name='agenda/show_event.html'
    )  # noqa


def enjoy_event(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(Event, id=event_id)
    event.participants += 1
    event.save()

    return HttpResponseRedirect(reverse('show-event', args=(event.id, )))
    # f'/event/{event.id}'

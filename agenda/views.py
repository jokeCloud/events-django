from django.shortcuts import render

from agenda.models import Event

# from django.template import loader


def list_events(request):
    events = Event.objects.all()
    return render(
        request=request,
        context={'events': events},
        template_name='agenda/list_events.html'
    )  # noqa


def show_event(request):
    event = {
        'name': 'Python class',
        'category': 'backend',
        'local': 'Louisiana',
    }
    # template = loader.get_template('agenda/show_event.html')
    # rendered_template = template.render(
    #    context={'event': event}, request=request)
    # return HttpResponse(rendered_template)
    return render(request=request, context={'event': event}, template_name='agenda/show_event.html')  # noqa

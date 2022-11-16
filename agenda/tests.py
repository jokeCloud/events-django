from datetime import date

from django.test import Client, TestCase

from agenda.models import Category, Event


# Create your tests here.
class TestInitialPage(TestCase):
    def test_events_list(self):
        client = Client()
        response = client.get('/')
        # self.assertContains(response, '<th>Name</th>')
        self.assertTemplateUsed(response, 'agenda/list_events.html')


class TestEventsListing(TestCase):
    def test_event_from_today_printed(self):
        category = Category()
        category.name = 'Backend'
        category.save()

        event = Event()
        event.name = 'Python Class'
        event.category = category
        event.local = 'Louisiana'
        event.date = date.today()
        event.save()

        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Python Class')
        self.assertEqual(list(response.context['events']), [event])

    def test_event_without_date_its_show(self):
        category = Category()
        category.name = 'Backend'
        category.save()

        event = Event()
        event.name = 'Python Class'
        event.category = category
        event.local = 'Louisiana'
        event.date = None
        event.save()

        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Python Class')
        self.assertContains(response, 'to be defined.')
        self.assertEqual(list(response.context['events']), [event])

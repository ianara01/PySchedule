from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from .models import Schedule

class ScheduleViewsTest(TestCase):
    def setUp(self):
        Schedule.objects.create(title="Test Schedule", date="2024-11-28", priority="High")

    def test_schedule_list_view(self):
        response = self.client.get(reverse('schedule:schedule_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Schedule")

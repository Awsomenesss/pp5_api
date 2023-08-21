from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, time, date


class EventListTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_events(self):
        adam = User.objects.get(username='adam')
        Event.objects.create(
            owner=adam,
            description='an event description',
            date=date.today(),
            time=time(14, 30)
        )
        response = self.client.get('/event/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/event/', {
            'description': 'an event description',
            'date': date.today(),
            'time': time(14, 30),
            'location': 'Event location'
        })
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_event(self):
        response = self.client.post('/event/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

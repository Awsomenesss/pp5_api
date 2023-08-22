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
        response = self.client.post('/event/', {
            'description': 'an event description',
            'date': date.today(),
            'time': time(14, 30),
            'location': 'Event location'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        event1 = Event.objects.create(
            owner=adam,
            description='an event description',
            date=date.today(),
            time=time(14, 30),
            location='Event location'
        )
        event2 = Event.objects.create(
            owner=brian,
            description='another event description',
            date=date.today(),
            time=time(14, 30),
            location='Event location'
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/event/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'an event description')

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/event/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/event/1/', {
            'description': 'updated event description',
            'date': date.today(),
            'time': time(14, 30),
            'location': 'Updated Event location'
        })
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.description, 'updated event description')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_event(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/event/2/', {
            'description': 'an updated event description',
            'date': date.today(),
            'time': time(14, 30),
            'location': 'Updated Event location'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

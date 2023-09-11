from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from events.models import Event, Reservation
from django.contrib.auth.models import User
from events.views import check_data_and_delete


class EventViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create an event
        self.event = Event.objects.create(
            title="Test Event", start_date=timezone.now() + timezone.timedelta(days=1)
        )

    def test_index_view_post(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        response = self.client.post(reverse("index"), {"id": self.event.id})

        # Check if the reservation was created
        self.assertEqual(response.status_code, 302)  # Redirects to 'management' view

        reservation = Reservation.objects.filter(user=self.user, event=self.event)
        self.assertTrue(reservation.exists())

    def test_management_view(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        response = self.client.get(reverse("management"))

        # Check if the 'management' view returns a successful response
        self.assertEqual(response.status_code, 200)

    def test_delete_view(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        reservation = Reservation.objects.create(user=self.user, event=self.event)

        response = self.client.post(reverse("delete"), {"id": reservation.id})

        # Check if the reservation is deleted
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reservation.objects.filter(id=reservation.id).exists())

    def test_check_data_and_delete(self):
        # Create a reservation
        reservation = Reservation.objects.create(user=self.user, event=self.event)

        # Check if the reservation is not expired
        self.assertFalse(check_data_and_delete(reservation))

        # Make the event start time 3 days ago (expired)
        self.event.start_date = timezone.now() - timezone.timedelta(days=3)
        self.event.save()

        # Check if the reservation is expired
        self.assertTrue(check_data_and_delete(reservation))

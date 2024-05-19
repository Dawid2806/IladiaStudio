from django.test import TestCase
from .models import TattoClients, Appointment
from django.core.exceptions import ValidationError


class AppointmentTestCase(TestCase):
    def setUp(self):
        self.client = TattoClients.objects.create(
            firstname="John", lastname="Doe", birthdate="1980-01-01",
            phone="123456789", streetAndNumber="123 Main St",
            city="Anytown", postcode="12345"
        )
        self.appointment = Appointment.objects.create(
            client=self.client, start_time="2024-05-20T10:00:00Z",
            end_time="2024-05-20T11:00:00Z", is_private=False
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.client.firstname, "John")
        self.assertEqual(str(self.appointment), f"Appointment with {self.client} on 2024-05-20 10:00:00+00:00")

    def test_appointment_overlap_validation(self):
        with self.assertRaises(ValidationError):
            overlapping_appointment = Appointment(
                client=self.client, start_time="2024-05-20T10:30:00Z",
                end_time="2024-05-20T11:30:00Z", is_private=False
            )
            overlapping_appointment.clean()

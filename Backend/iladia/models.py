from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=50)


class TattoClients(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    streetAndNumber = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class TattoHealthDeclaration(models.Model):
    client = models.ForeignKey(TattoClients, on_delete=models.CASCADE)
    declaration_text = models.TextField()
    signature_base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Health Declaration for {self.client.firstname} {self.client.lastname}"


class DataPrivacyAgreement(models.Model):
    client = models.ForeignKey(TattoClients, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    signature_base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data Privacy Agreement for {self.client.firstname} {self.client.lastname}"


class Appointment(models.Model):
    client = models.ForeignKey(TattoClients, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.client:
            return f"Appointment with {self.client} on {self.start_time}"
        else:
            return f"Private appointment on {self.start_time}"

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        overlapping_appointments = Appointment.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)
        if overlapping_appointments.exists():
            raise ValidationError("This appointment overlaps with another appointment.")


class NailsClients(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthdate = models.DateField()
    phone = models.CharField(max_length=50)
    streetAndNumber = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class DataPrivacyAgreementNails(models.Model):
    client = models.ForeignKey(NailsClients, on_delete=models.CASCADE)
    agreement_text = models.TextField()
    signature_base64 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data Privacy Agreement for {self.client.firstname} {self.client.lastname}"


class AppointmentNails(models.Model):
    client = models.ForeignKey(NailsClients, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.client:
            return f"Appointment with {self.client} on {self.start_time}"
        else:
            return f"Private appointment on {self.start_time}"

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")
        overlapping_appointments = Appointment.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)
        if overlapping_appointments.exists():
            raise ValidationError("This appointment overlaps with another appointment.")
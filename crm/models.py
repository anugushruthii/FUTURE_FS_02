from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    LEAD = 'lead'
    CUSTOMER = 'customer'
    PROSPECT = 'prospect'
    STATUS_CHOICES = [
        (LEAD, 'Lead'),
        (CUSTOMER, 'Customer'),
        (PROSPECT, 'Prospect'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=LEAD)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

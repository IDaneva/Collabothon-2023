from django.db import models
from django.utils import timezone


CATEGORIES = [
    ("Shopping", "Shopping"),
    ("Groceries", "Groceries"),
    ("Restaurants", "Restaurants"),
    ("Transport", "Transport"),
    ("Cash", "Cash"),
    ("Travel", "Travel"),
    ("Health", "Health"),
    ("Transfers", "Transfers"),
    ("Other", "Other"),
]

GENDERS = [
    ("Male", "Male"),
    ("Female", "Female")
]

TYPES = [
    ("Personal", "Personal"),
    ("Family", "Family")
]


class Customer(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(default=timezone.now)
    personal_number = models.CharField(max_length=15, default="0000000000")
    gender = models.CharField(max_length=20, choices=GENDERS, default="Male")

    def __str__(self):
        return self.name


class Account(models.Model):
    holder = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=20)
    amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(Customer, related_name="members", blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPES, blank=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.number)


class Income(models.Model):
    affected_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.amount)


class Spends(models.Model):
    affected_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.amount)

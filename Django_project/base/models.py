from django.db import models

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


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Account(models.Model):
    holder = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    number = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)


class Income(models.Model):
    affected_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.amount)


class Spends(models.Model):
    affected_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=50,choices=CATEGORIES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.amount)


from django.contrib import admin
from .models import Account, Customer, Transactions

admin.site.register(Account)
admin.site.register(Transactions)
admin.site.register(Customer)


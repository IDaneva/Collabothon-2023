from django.contrib import admin
from .models import Account, Customer, Transaction

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Customer)


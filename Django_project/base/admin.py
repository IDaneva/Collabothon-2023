from django.contrib import admin
from .models import Account, Income, Spends, Customer

admin.site.register(Account)
admin.site.register(Income)
admin.site.register(Spends)
admin.site.register(Customer)


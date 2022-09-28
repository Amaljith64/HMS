from django.contrib import admin

from Payments.models import *


# Register your models here.
admin.site.register(PaymentClass)
admin.site.register(WalletDetails)
admin.site.register(MyWallet)
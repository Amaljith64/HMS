from sre_constants import CATEGORY
from django.contrib import admin

from AdminPanel.models import *

# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Rooms)
admin.site.register(HotelBookings)
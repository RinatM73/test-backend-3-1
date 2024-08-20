from django.contrib import admin

from users.models import *

admin.register(CustomUser)
admin.register(Balance)
admin.register(Subscription)

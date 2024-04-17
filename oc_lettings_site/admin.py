from django.contrib import admin

from letting.models import Letting, Addres
from user_profile.models import Profile


admin.site.register(Letting)
admin.site.register(Addres)
admin.site.register(Profile)

from django.contrib import admin
from .models import UserProfile,Newsletter,Contact,Issue
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Issue)
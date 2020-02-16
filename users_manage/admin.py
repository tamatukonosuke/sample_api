from django.contrib import admin

from .models import User, Entry


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

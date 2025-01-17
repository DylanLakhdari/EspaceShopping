from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["email", "username","first_name","last_name"]

    fieldsets = UserAdmin.fieldsets + (
            ("Champs additionnels", {'fields': ('profile_picture',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
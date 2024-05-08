from django.urls import path

from .views import signup, user_settings, user_delete

urlpatterns = [
    path("signup/", signup.as_view(), name="accounts-signup"),
    path("settings/<str:username>/", user_settings, name = 'accounts-user-settings'),
    path("user-delete/", user_delete, name="accounts-user-delete")
]

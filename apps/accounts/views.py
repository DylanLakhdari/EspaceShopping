from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from accounts.models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
class signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def user_settings(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.user != user:
        return HttpResponseForbidden()
    return render(request, "user_settings.html")
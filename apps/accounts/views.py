from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
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
    form = CustomUserChangeForm(request.POST, instance=user)

    if request.user != user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('accounts-user-settings', username)
        
    return render(request, "catalog/user_settings.html",  {'form': form})

@login_required
def user_delete(request):
    user = get_object_or_404(CustomUser, username=request.user.username)
    
    user.delete()

    return redirect('catalog-index')
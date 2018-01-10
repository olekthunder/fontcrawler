from itertools import chain

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from main.models import Font

from .forms import ProfileForm, UserForm


def _form_errors_to_messages(request, form_errors):
    """Not a view. Converts form errors to django message"""
    for error_text in chain(*form_errors.values()):
        messages.error(request, error_text)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                request,
                username=username,
                password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
        else:
            _form_errors_to_messages(request, form.errors)
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
        else:
            _form_errors_to_messages(request, form.errors)
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'registration/sign_in.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    messages.success(request, "You've been successfully logged out!")
    return redirect('home')


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'registration/profile.html'
    context_object_name = 'font_list'
    model = Font
    paginate_by = 25

    def get_queryset(self):
        """
            Overrides method to get only objects
            related to current user logged in
        """
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """
            Overrides method to get context dict
            and extend it
        """
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_form = UserForm(instance=self.request.user)
        profile_form = ProfileForm(instance=self.request.user.profile)
        extra_context = {
            'user': self.request.user,
            'user_form': user_form,
            'profile_form': profile_form
        }
        context.update(extra_context)
        return context


class AuthRedirect(View):
    """Checks if user is authenticated"""

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('accounts:profile')
        else:
            return redirect('accounts:sign_in')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('accounts:profile')
        else:
            _form_errors_to_messages(request, user_form.errors)
            _form_errors_to_messages(request, profile_form.errors)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

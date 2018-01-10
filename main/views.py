from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, RedirectView

from accounts.views import _form_errors_to_messages

from .forms import ParsePageForm
from .models import Font
from .tasks import parse_page


@login_required
def add_font(request):
    parse_page.delay(request.user.id, 'http://github.com/')
    messages.success(
        request,
        'Your request will be processed soon, check your profile')
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ParsePageForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data.get('url')
                parse_page.delay(request.user.id, url)
                messages.success(
                    request, 'Your request will be processed soon, check your profile')
            else:
                _form_errors_to_messages(request, form.errors)
        else:
            form = ParsePageForm()
    else:
        form = None
    return render(request, 'main/home.html', {'form': form})


class FontListView(ListView):
    model = Font
    context_object_name = 'font_list'
    paginate_by = 3
    template_name = 'main/font_list.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class HomeRedirect(RedirectView):
    pattern_name = 'home'

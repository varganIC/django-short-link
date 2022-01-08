from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Link
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'short_link/home.html')


def contact(request):
    return render(request, 'short_link/contact.html')


class CreateLink(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'short_link/short.html'

    fields = ['lohg_link', 'short']

    def form_valid(self, form):
        form.instance.id_user = self.request.user
        form.instance.short_link = settings.SITE_URL + '/' + form.cleaned_data.get('short')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateLink, self).get_context_data(**kwargs)
        ctx['link'] = Link.objects.filter(id_user=self.request.user)
        return ctx


def redirect_original(request, pk):
    url = get_object_or_404(Link, pk=pk)
    return HttpResponseRedirect(url.lohg_link)
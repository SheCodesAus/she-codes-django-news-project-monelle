from wsgiref.handlers import format_date_time
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfile(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('userProfile')
    template_name = 'users/userprofile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context


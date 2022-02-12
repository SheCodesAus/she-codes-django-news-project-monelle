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

def get_current_user(request):
    user = request.user
    return render(request, 'users/userProfile.html', {"user":user})
    
class UserProfile(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('userProfile')
    template_name = 'users/userProfile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context


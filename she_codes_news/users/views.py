from wsgiref.handlers import format_date_time
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .models import CustomUser
from news.models import NewsStory
from django.views import generic
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

def get_current_user(request):
    user = request.user
    return render(request, 'users/userProfile.html', {"user":user})

    
class UserProfileView(generic.DetailView):
        template_name = 'users/userProfile.html'
        model = CustomUser


class PostLogin(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('users:userProfile', kwargs={'pk':self.request.user.id})

from django.urls import path
from .views import CreateAccountView, UserProfile, UpdateView

app_name = 'users'

urlpatterns = [ 
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('userProfile/', UserProfile.as_view(), name='userProfile'),
]
from django.urls import path
from .views import CreateAccountView, UserProfile, get_current_user

app_name = 'users'

urlpatterns = [ 
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('userProfile/', get_current_user, name='userProfile'),
    path('userProfile/<int:pk>', UserProfile.as_view(), name='userProfile'),



]
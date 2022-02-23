from django.urls import path
from .views import CreateAccountView, UserProfileView, get_current_user, PostLogin

app_name = 'users'

urlpatterns = [ 
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('userProfile/', get_current_user, name='userProfile'),
    path('user/<int:pk>', UserProfileView.as_view(), name='userProfile'),
    path('user/my_profile', PostLogin.as_view(), name='my-profile'),
]
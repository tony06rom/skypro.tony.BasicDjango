from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserRegisterView, email_verification
from django.urls import path


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/user_login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(template_name='users/user_logout.html', next_page='/catalog/products_list/'), name='user_logout'),
    path('register/', UserRegisterView.as_view(template_name='users/user_register.html'), name='user_register'),
    path('email-confirm/<str:token>', email_verification, name='email-confirm'),
]

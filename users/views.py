from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
import secrets
from django.views.generic.edit import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import CustomUser

class UserRegisterView(CreateView):
    model = CustomUser
    template_name='users/user_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтверждение регистрации",
            message="Здравствуйте! Пройдите по ссылке для подтверждения регистрации",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    return redirect(reverse("users:user_login"))

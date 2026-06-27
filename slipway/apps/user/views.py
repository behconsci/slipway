from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "user/login.html"


class SignUpView(TemplateView):
    template_name = "user/signup.html"


class SignUpConfirmView(TemplateView):
    template_name = "user/signup_confirm.html"

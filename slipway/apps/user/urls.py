from django.urls import path

from .views import LoginView, SignUpConfirmView, SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/confirm/", SignUpConfirmView.as_view(), name="signup-confirm"),
]

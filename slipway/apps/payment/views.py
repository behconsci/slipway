from django.views.generic import TemplateView


class StripePaymentView(TemplateView):
    template_name = "payment/stripe_payment.html"

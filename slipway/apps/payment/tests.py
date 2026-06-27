from django.test import SimpleTestCase


class PaymentPageTests(SimpleTestCase):
    def test_stripe_payment_page(self):
        response = self.client.get("/payment/stripe/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add payment method")
        self.assertContains(response, "Stripe")
        self.assertContains(response, "cdn.tailwindcss.com")

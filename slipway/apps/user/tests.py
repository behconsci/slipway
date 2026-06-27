from django.test import SimpleTestCase


class UserPageTests(SimpleTestCase):
    def test_login_page_uses_tailwind_template(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome back")
        self.assertContains(response, "cdn.tailwindcss.com")

    def test_signup_page_uses_tailwind_template(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create your account")
        self.assertContains(response, "one-time confirmation code")

    def test_signup_confirm_page_has_one_time_code(self):
        response = self.client.get("/signup/confirm/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter the one-time code")

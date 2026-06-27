from django.conf import settings
from django.test import SimpleTestCase


class ProjectStructureTests(SimpleTestCase):
    def test_required_apps_installed(self):
        required_apps = {
            "slipway.apps.core",
            "slipway.apps.user",
            "slipway.apps.app",
            "slipway.apps.payment",
        }

        self.assertTrue(required_apps.issubset(set(settings.INSTALLED_APPS)))

    def test_site_static_dir_is_configured(self):
        self.assertIn(settings.BASE_DIR / "site-static", settings.STATICFILES_DIRS)

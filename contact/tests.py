from django.test import TestCase

# Functional tests
class ContactViewsTestCase(TestCase):
    def test_form_contact_is_visible(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

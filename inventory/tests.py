from django.test import TestCase

from inventory.models import Item

class ItemsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/items_list/')
        self.assertEqual(resp.status_code, 200)
#        self.assertTrue('latest_poll_list' in resp.context)

class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_basic_sub(self):
        self.assertEqual(2 - 1, 1)

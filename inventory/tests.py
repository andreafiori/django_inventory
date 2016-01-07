from django.test import TestCase

from inventory.models import Item

class ItemsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_items_pagination(self):
	resp = self.client.get('/items_pagination/')
        self.assertEqual(resp.status_code, 200)

    def test_items_list(self):
	resp = self.client.get('/items_list/')
        self.assertEqual(resp.status_code, 200)


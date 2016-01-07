import unittest
import mock
from django.db import models
from django.test import TestCase

from inventory.models import Item

# Functional tests
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

# Mock and test Item model
class ItemTests(unittest.TestCase):
    def test_title_can_be_set(self):
        item = mock.Mock(spec=Item)
	item.title = 'My item title'
	self.assertEqual('My item title', item.title)

    def test_description_can_be_set(self):
        item = mock.Mock(spec=Item)
	item.description = 'My item description'
	self.assertEqual('My item description', item.description)

    def test_amount_can_be_set(self):
        item = mock.Mock(spec=Item)
	item.amount = 'My item amount'
	self.assertEqual('My item amount', item.amount)

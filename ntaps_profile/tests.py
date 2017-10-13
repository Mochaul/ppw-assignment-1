from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
from django.http import HttpRequest
from unittest import skip

class ProfileUnitTest(TestCase):

    def test_profile_url_is_exist(self):
        response = Client().get('/profile/')
        self.assertEqual(response.status_code, 200)

    #def test_expertise_more_than_6(self):
    #   self.assertTrue(len(expertise) >= 6)

    def test_profile_using_index_func(self):
        found = resolve('/profile/')
        self.assertEqual(found.func, index)

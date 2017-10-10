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

    @skip("Masih in progress") # Kalo udah jadi testnya ilangin baris ini
    def test_about_me_more_than_6(self):
       self.assertTrue(len(about_me) >= 6)

    def test_profile_using_index_func(self):
        found = resolve('/profile/')
        self.assertEqual(found.func, index)

    @skip("Masih in progress") # Kalo udah jadi testnya ilangin baris ini
    def test_landing_page_is_completed(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')

        #Checking whether have Bio content
        self.assertIn(landing_page_content, html_response)

        #Chceking whether all About Me Item is rendered
        for item in about_me:
            self.assertIn(item,html_response)

from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, create, append_http
from .models import Friend
from .forms import Add_Friend_Form

# Create your tests here.
class AddFriendUnitTest(TestCase):

    def test_add_friend_url_is_exist(self):
        response = Client().get('/add_friend/')
        self.assertEqual(response.status_code, 200)

    def test_add_friend_using_index_func(self):
        found = resolve('/add_friend/')
        self.assertEqual(found.func, index)

    def test_model_can_create_new_Friend(self):
        new_friend = Friend.objects.create(name='Teman Baru', url='http://website.teman.baru')
        counting_all_available_friend = Friend.objects.all().count()
        self.assertEqual(counting_all_available_friend, 1)

    def test_form_add_friend_input_has_placeholder_and_css_classes(self):
        form = Add_Friend_Form()
        self.assertIn('class="input-text', form.as_p())
        self.assertIn('id="id_name"', form.as_p())
        self.assertIn('class="input-text-inline-button', form.as_p())
        self.assertIn('id="id_url', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = Add_Friend_Form(data={'name': '', 'url': ''})
        self.assertFalse(form.is_valid())

    def test_add_friend_post_success_and_render_the_result(self):
        test = 'google.com'
        response_post = Client().post('/add_friend/create/', {'name': test, 'url': test})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)

    def test_add_friend_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/add_friend/create/', {'name': '', 'url': ''})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_add_friend_url_invalid(self):
        test = 'Anonymous'
        response_post = Client().post('/add_friend/create/', {'name': test, 'url': test})
        self.assertEqual(response_post.status_code, 302)

        self.assertIn('Url temanmu tidak bisa diakses. Format URL: http://ntaps.herokuapp.com', response_post.cookies['messages'].value)

    def test_append_url(self):
        expected = 'http://google.com'

        url = 'google.com'
        http_url = 'http://google.com'

        appended_url = append_http(url)
        appended_http_url = append_http(http_url)

        self.assertEqual(appended_url, expected)
        self.assertEqual(appended_http_url, expected)

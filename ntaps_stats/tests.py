from django.test import TestCase
from django.test import Client
from django.urls import resolve
from ntaps_stats.views import index
from ntaps_add_friend.models import Friend
from ntaps_update_status.models import Status
from ntaps_profile.views import name

# Create your tests here.
class StatsUnitTest(TestCase):
  def test_add_friend_url_is_exist(self):
    response = Client().get('/stats/')
    self.assertEqual(response.status_code, 200)

  def test_add_friend_using_index_func(self):
    found = resolve('/stats/')
    self.assertEqual(found.func, index)

  def test_content_is_rendered(self):
    Friend.objects.create(name="test friend", url="google.com").save()
    Status.objects.create(status="test status").save()

    response = Client().get('/stats/')
    html_response = response.content.decode('utf8')
    self.assertIn(str(Friend.objects.count()),html_response)
    self.assertIn(str(Status.objects.count()),html_response)
    self.assertIn(name,html_response)

from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .models import Status, Comment
from .views import index
from .forms import Status_Form, Comment_Form

# Create your tests here.
class UpdateStatusUnitTest(TestCase):

	def test_update_status_url_is_exist(self):
		response = Client().get('/update_status/')
		self.assertEqual(response.status_code, 200)

	def test_update_status_using_index_func(self):
		found = resolve('/update_status/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_status_and_has_str_function(self):
		new_activity = Status.objects.create(status='menulis status harian')
		counting_all_available_status=Status.objects.all().count()
		self.assertEqual(counting_all_available_status,1)
		self.assertEqual(str(new_activity), new_activity.status)

	def test_model_can_create_new_comment_and_has_str_function(self):
		new_activity = Comment.objects.create(comment='menulis comment di status')
		counting_all_available_comment=Comment.objects.all().count()
		self.assertEqual(counting_all_available_comment,1)
		self.assertEqual(str(new_activity), new_activity.comment)

	def test_form_status_input_has_placeholder_and_css_classes(self):
	    form = Status_Form()
	    self.assertIn('class="status-form-textarea', form.as_p())
	    self.assertIn('id="id_status', form.as_p())

	def test_form_validation_for_blank_items(self):
	    form = Status_Form(data={'status':''})
	    self.assertFalse(form.is_valid())
	    self.assertEqual(
	        form.errors['status'],
	        ["This field is required."]
	    )
	def test_update_status_post_success_and_render_the_result(self):
	    test = 'Anonymous'
	    response_post = Client().post('/update_status/add_status', {'status': test})
	    self.assertEqual(response_post.status_code, 302)

	    response= Client().get('/update_status/')
	    html_response = response.content.decode('utf8')
	    self.assertIn(test, html_response)

	def test_update_status_post_error_and_render_the_result(self):
	    test = 'Anonymous'
	    response_post = Client().post('/update_status/add_status', {'status': ''})
	    self.assertEqual(response_post.status_code, 302)

	    response= Client().get('/update_status/')
	    html_response = response.content.decode('utf8')
	    self.assertNotIn(test, html_response)

	def test_update_status_delete_todo(self):
		status = Status(status='ini akan didelete')
		status.save()
		response = Client().get('/update_status/delete_status/{}'.format(status.id))
		html_response = response.content.decode('utf8')
		self.assertNotIn(status.status, html_response)

#	def test_lab5_access_delete_todo_via_get(self):
#		response = Client().get('/update_status/delete_status')
#		html_response = response.content.decode('utf8')
#		self.assertRedirects(response,'/update_status/',302,200)

	def test_form_comment_input_has_placeholder_and_css_classes(self):
	    form = Comment_Form()
	    self.assertIn('class="comment-form-textarea', form.as_p())
	    self.assertIn('id="id_comment', form.as_p())

	def test_add_comment(self):
		status = Status(status='ini akan dicomment')
		status.save()
		response_post = Client().post('/update_status/add_comment/{}/'.format(status.id), data={'comment':'ini comment'})
		response = Client().get('/update_status/')
		html_response = response.content.decode('utf8')
		self.assertIn('ini comment', html_response)

	def test_add_comment_error(self):
		status = Status(status='ini akan dicomment')
		status.save()
		response_post = Client().post('/update_status/add_comment/{}/'.format(status.id), data={'comment':''})
		response = Client().get('/update_status/')
		html_response = response.content.decode('utf8')
		self.assertNotIn('ini comment', html_response)

	# def test_update_comment_post_success_and_render_the_result(self):
	#     test = 'Anonymous'
	#     response_post = Client().post('/update_status/add_comment', {'comment': test})
	#     self.assertEqual(response_post.status_code, 302)

	#     response= Client().get('/update_status/')
	#     html_response = response.content.decode('utf8')
	#     self.assertIn(test, html_response)

	# def test_update_comment_post_error_and_render_the_result(self):
	#     test = 'Anonymous'
	#     response_post = Client().post('/update_status/add_comment', {'comment': ''})
	#     self.assertEqual(response_post.status_code, 302)

	#     response= Client().get('/update_status/')
	#     html_response = response.content.decode('utf8')
	#     self.assertNotIn(test, html_response)

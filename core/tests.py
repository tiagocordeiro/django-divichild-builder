import io
import zipfile

from django.test import RequestFactory, TestCase, Client

from .forms import ChildForm
from .views import home


class ChildFormTests(TestCase):
    def test_valid_form(self):
        data = {
            'child_name': 'MeuTema',
            'customer_name': 'Meu Cliente',
            'customer_site': 'https://example.com',
        }
        form = ChildForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_url(self):
        data = {
            'child_name': 'MeuTema',
            'customer_name': 'Meu Cliente',
            'customer_site': 'nao-eh-url',
        }
        form = ChildForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('customer_site', form.errors)

    def test_child_name_max_length(self):
        data = {
            'child_name': 'A' * 31,
            'customer_name': 'Meu Cliente',
            'customer_site': 'https://example.com',
        }
        form = ChildForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('child_name', form.errors)

    def test_customer_name_max_length(self):
        data = {
            'child_name': 'MeuTema',
            'customer_name': 'A' * 31,
            'customer_site': 'https://example.com',
        }
        form = ChildForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('customer_name', form.errors)

    def test_required_fields(self):
        form = ChildForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('child_name', form.errors)
        self.assertIn('customer_name', form.errors)
        self.assertIn('customer_site', form.errors)


class HomeViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_get_status_ok(self):
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_home_get_has_form_in_context(self):
        response = self.client.get('/')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ChildForm)

    def test_home_post_valid_stores_session(self):
        data = {
            'child_name': 'MeuTema',
            'customer_name': 'Meu Cliente',
            'customer_site': 'https://example.com',
        }
        self.client.post('/', data)
        self.assertEqual(self.client.session['child_name'], 'MeuTema')
        self.assertEqual(self.client.session['customer_name'], 'Meu Cliente')
        self.assertEqual(self.client.session['customer_site'], 'https://example.com')

    def test_home_post_invalid_rerenders_with_errors(self):
        data = {
            'child_name': '',
            'customer_name': '',
            'customer_site': 'invalido',
        }
        response = self.client.post('/', data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())


class DownloadChildViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_data = {
            'child_name': 'MeuTema',
            'customer_name': 'Meu Cliente',
            'customer_site': 'https://example.com',
        }

    def test_download_returns_ok(self):
        response = self.client.post('/download-child/', self.valid_data)
        self.assertEqual(response.status_code, 200)

    def test_download_content_type_is_zip(self):
        response = self.client.post('/download-child/', self.valid_data)
        self.assertEqual(response['Content-Type'], 'application/x-zip-compressed')

    def test_download_content_disposition_has_filename(self):
        response = self.client.post('/download-child/', self.valid_data)
        self.assertIn('MeuTema.zip', response['Content-Disposition'])

    def test_download_response_is_valid_zip(self):
        response = self.client.post('/download-child/', self.valid_data)
        self.assertTrue(zipfile.is_zipfile(io.BytesIO(response.content)))

    def test_download_uses_defaults_without_post_data(self):
        response = self.client.post('/download-child/', {})
        self.assertEqual(response.status_code, 200)
        self.assertIn('DiviChild.zip', response['Content-Disposition'])

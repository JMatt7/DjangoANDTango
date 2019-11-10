from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        respons = self.client.get('/')
        self.assertEqual(respons.status_code, 200)
    def test_about_page_status_code(self):
        respons = self.client.get('/about/')
        self.assertEqual(respons.status_code, 200)
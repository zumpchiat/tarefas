from django.test import TestCase


# Create your tests here.

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads no autorized task"""
        response = self.client.get('http://localhost:8000')
        self.assertEqual(response.status_code, 302)

    def test_index_loads_about(self):
        """The index page loads about"""
        response = self.client.get('http://localhost:8000/about/')
        self.assertEqual(response.status_code, 200)

    def test_index_loads_admin(self):
        """The index page loads ADM"""
        response = self.client.get('http://localhost:8000/admin')
        self.assertEqual(response.status_code, 301)
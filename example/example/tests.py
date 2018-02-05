from django.test import TestCase


class TestSimpleView(TestCase):
    def test_simple_view(self):
        response = self.client.get('/simple/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello, Test!\n')

    def test_simple_view_with_name(self):
        response = self.client.get('/simple/xxx')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello, xxx!\n')

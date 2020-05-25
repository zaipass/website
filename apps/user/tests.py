from django.test import TestCase


class SimpleTest(TestCase):
    """测试首页网址"""

    def test_index(self):
        print('---------**********')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from .models import UrlDetailes

""" Test module for UrlDetailes model """


class UrlDetailesTest(TestCase):
    def setUp(self):
        UrlDetailes.objects.create(
            original_url='http://www.google.com')
        UrlDetailes.objects.create(
            original_url='http://www.yahoo.com')

    def test_get_objects(self):
        UrlDetailes_gooogle = UrlDetailes.objects.get(
            original_url='http://www.google.com')
        UrlDetailes_yahoo = UrlDetailes.objects.get(
            original_url='http://www.yahoo.com')
        self.assertEqual(
            UrlDetailes_gooogle.object_check(), 'original url http://www.google.com')
        self.assertEqual(
            UrlDetailes_yahoo.object_check(), 'original url http://www.yahoo.com')

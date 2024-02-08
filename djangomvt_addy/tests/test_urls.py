from django.test import SimpleTestCase,Client
from django.urls import reverse,resolve
from djangomvt_addy.views import fun2,fun,home

class TestUrls(SimpleTestCase):

    def test_myproject_url(self):
        url = reverse('myproject')
        print(resolve(url))
        self.assertEqual(resolve(url).func,fun)

    def test_myproject_Form_url(self):
        url1 = reverse('myproject_Form')
        # print(resolve(url1))
        self.assertEqual(resolve(url1).func,fun2)

    def test_home_url(self):
        url1 = reverse('home')
        # print(resolve(url1))
        self.assertEqual(resolve(url1).func,home)
               


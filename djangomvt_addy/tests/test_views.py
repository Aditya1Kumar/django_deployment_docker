from django.urls import reverse
from django.test import TestCase,Client


class myTC(TestCase):
    def setUp(self) -> None:
        self.client=Client()
        return super().setUp()
    def test_validatemovie(self):
        
        response=self.client.get(reverse('myproject'))
        print(response)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'myproject.html')


    # def test_equal(self):
    #     self.assertEqual(1 , 1)
    # def test_notequal(self):
    #     self.assertEqual(1 , 2)
    # def test3(self):
    #     response=self.client.get(reverse('myproject'))
    #     self.assertTrue(response,'failure')
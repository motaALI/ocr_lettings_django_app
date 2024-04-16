# # test_views.py
# from django.test import Client, TestCase
# from django.urls import reverse
# from unittest.mock import patch

# import pytest

# from letting.models import Addres, Letting
# from tests.factories import LettingFactory

# class ViewsTest(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_index_view(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)

#     def test_lettings_index_view(self):
#         response = self.client.get(reverse('lettings_index'))
#         self.assertEqual(response.status_code, 200)

#     # def test_letting_view(self):
#     #     # Replace 1 with the actual letting_id you want to test
#     #     response = self.client.get(reverse('letting', args=[1]))
#     #     self.assertEqual(response.status_code, 200)

#     def test_profiles_index_view(self):
#         response = self.client.get(reverse('profiles_index'))
#         self.assertEqual(response.status_code, 200)

#     # def test_profile_view(self):
#     #     # Replace 'testuser' with the actual username you want to test
#     #     response = self.client.get(reverse('profile', args=['testuser']))
#     #     self.assertEqual(response.status_code, 200)

# @pytest.mark.django_db
# @patch.object(Letting.objects, 'get')
# def test_letting_view_use_factories(mock_get):
#     # Replace 1 with the actual letting_id you want to test

#     # letting = LettingFactory(title='Mock Title', address=Addres(id=1, street='Mock Addres'))
#     letting = LettingFactory(title='Mock Title')
#     mock_get.return_value = letting

#     client = Client()
#     response = client.get(reverse('letting', args=[1]))

#     assert response.status_code == 200
#     assert 'Mock Title' in response.content.decode('utf-8')
#     # assert 'Mock Addres' in response.content.decode('utf-8')
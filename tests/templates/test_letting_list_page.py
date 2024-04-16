# # test_templates.py
# # test_templates.py
# from django.test import Client
# from django.test import TestCase
# from django.urls import reverse
# from django.template import Template, Context
# from letting.views import lettings_index 


# class TestLettingListTemplate(TestCase):
    
#     def setUp(self):
#         self.client = Client()
        
#     def test_home_template(self):
#         response = self.client.get(reverse('lettings_index'))  # Use reverse to get the URL
#         self.assertEqual(response.status_code, 200)

#         template = Template(response.content.decode('utf-8'))
#         context = Context()
#         rendered_content = template.render(context)

#         # Check if the title is present
        
#         print(f"context : {rendered_content}")
#         # assert 'Your Title' in rendered_content

#         # # Check if the address information is present
#         # assert '123 Main St' in rendered_content
#         # assert 'City Name, ST 12345' in rendered_content
#         # assert 'USA' in rendered_content

#         # Check if the Back, Home, and Profiles links are present
#         # assert 'href="' + reverse('lettings_index') + '"' in rendered_content
#         # assert 'href="' + reverse('index') + '"' in rendered_content
#         # assert 'href="' + reverse('profiles_index') + '"' in rendered_content
#         self.assertInHTML('<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>', rendered_content)
#         self.assertInHTML('<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/">Home</a>', rendered_content)
#         self.assertInHTML('<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/profiles/">Profiles</a>', rendered_content)



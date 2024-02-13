.. _unittest:
=======================
Test Documentation
=======================

Introduction
-----------------------
This documentation outlines the testing procedures for the `Address` model within the Letting application. The tests ensure that basic CRUD (Create, Read, Update, Delete) operations function correctly for the `Address` model.

Testing Environment
-----------------------
The tests are written in Python and leverage the Django framework for web application development. Additionally, the `pytest` library is used for testing.

Libraries Used
-----------------------
- `django.test.Client`: Django's test client for making requests to views during testing.
- `django.test.TestCase`: Django's built-in test case class for testing Django applications.
- `django.urls.reverse`: A function for generating URLs for Django views.
- `unittest.mock.patch`: A module for patching objects during testing.
- `pytest`: A testing framework that simplifies writing and executing tests in Python.


Test Cases Models
-----------------------
1. test_create_address
   - **Purpose:** This test verifies the creation of an `Address` instance.
   - **Procedure:**
     1. Create a new `Address` instance with specified attributes.
     2. Save the address.
     3. Assert that the address has been assigned a valid ID.
   - **Expected Outcome:** The address is successfully created, and an ID is assigned to it.

2. test_read_address
   - **Purpose:** This test verifies the retrieval of an existing `Address` instance from the database.
   - **Procedure:**
     1. Create a new `Address` instance with specified attributes.
     2. Save the address.
     3. Retrieve the address from the database using its ID.
   - **Expected Outcome:** The address is successfully retrieved from the database.

3. test_update_address
   - **Purpose:** This test verifies the update of an existing `Address` instance.
   - **Procedure:**
     1. Create a new `Address` instance with specified attributes.
     2. Save the address.
     3. Update the street attribute of the address.
     4. Retrieve the updated address from the database.
   - **Expected Outcome:** The address's street attribute is successfully updated.

4. test_delete_address
   - **Purpose:** This test verifies the deletion of an existing `Address` instance.
   - **Procedure:**
     1. Create a new `Address` instance with specified attributes.
     2. Save the address.
     3. Delete the address from the database.
     4. Attempt to retrieve the deleted address from the database.
   - **Expected Outcome:** The address is successfully deleted from the database.

5. TestAddressModel.test_str_method
   - **Purpose:** This test verifies the string representation of the `Address` model.
   - **Procedure:**
     1. Create an `Address` instance using a factory with specified attributes.
     2. Check the string representation of the address instance.
   - **Expected Outcome:** The string representation of the address matches the expected format.

Mocking
-----------------------
Mocking is not explicitly utilized in these tests. However, for future test cases that require mocking, the `unittest.mock` module in Python can be employed to simulate objects or functions.


Conclusion
-----------------------
These tests ensure the proper functioning of the `Address` model within the Letting application by validating basic CRUD operations and verifying the string representation of the model. Developers can execute these tests to ensure the stability and reliability of the application's address management functionality.


Test Cases URLs
-----------------------
1. `test_index_view`
   - **Purpose:** Verifies the response status code of the index view.
   - **Procedure:** Sends a GET request to the index view and checks if the response status code is 200.
   - **Expected Outcome:** The response status code should be 200.

2. `test_lettings_index_view`
   - **Purpose:** Verifies the response status code of the lettings index view.
   - **Procedure:** Sends a GET request to the lettings index view and checks if the response status code is 200.
   - **Expected Outcome:** The response status code should be 200.

3. `test_profiles_index_view`
   - **Purpose:** Verifies the response status code of the profiles index view.
   - **Procedure:** Sends a GET request to the profiles index view and checks if the response status code is 200.
   - **Expected Outcome:** The response status code should be 200.

Mocking
-----------------------
1. `test_letting_view_use_factories`
   - **Purpose:** Verifies the rendering of the letting view using factories.
   - **Procedure:**
     1. Creates a letting instance using a factory with a mock title.
     2. Mocks the `Letting.objects.get` method to return the created letting.
     3. Sends a GET request to the letting view.
   - **Expected Outcome:** The response status code should be 200, and the rendered content should contain the mock title.

Conclusion
-----------------------
These tests ensure the proper functioning of the views within the Django application by validating their response status codes and content. 
Developers can execute these tests to ensure the stability and reliability of the application's views.


Test Cases template
-----------------------
1. `test_letting_details_template`
   - **Purpose:** Verifies the rendering and context of the letting details template.
   - **Procedure:**
     1. Creates a Letting instance using a factory with mock data.
     2. Mocks the `letting.views.Letting.objects.get` method to return the created Letting instance.
     3. Sends a GET request to the letting details view.
     4. Asserts that the response status code is 200.
     5. Parses the response content as a template and renders it with an empty context.
     6. Asserts that the rendered content contains expected HTML elements and context variables.
     7. Asserts that the letting function was called with the correct arguments.
   - **Expected Outcome:** The template renders correctly with the expected context variables and HTML elements.

Conclusion
-----------------------
This test ensures that the letting details template in the Letting application renders correctly with the appropriate context variables. 
Developers can execute this test to ensure the stability and reliability of the letting details view.
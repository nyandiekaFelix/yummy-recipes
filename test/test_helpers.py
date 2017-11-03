from unittest import TestCase
from yummy_recipes.helpers import lower_email, lower_name, check_for_duplicate

class TestHelpers(TestCase):
    ''' Tests for helper methods '''

    def test_lower_email(self):
        ''' Should change the email to lowercase '''
        email = "NAME@domain.com"
        changed_email = lower_email(email)

        self.assertEqual('name@domain.com', changed_email)
    
    def test_lower_name(self):
        ''' Should convert name to lowerccase '''
        name = "SomeInterestingName"
        lower_case = "someinterestingname"

        self.assertEqual(lower_case, lower_name(name))
"""
This is code adapted from Corey Schafer's unittesting YouTube video.
"""

import unittest
from unittest.mock import patch
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    ### SET UP / TEAR DOWN ###

    @classmethod
    def setUpClass(cls):
        """
        Any code we want to run just once upfront for entire set of tests.
        """
        print('setupClass ')

    @classmethod
    def tearDownClass(cls):
        """
        Any code we want to run just once upon finishing entire set of tests.
        """
        print('teardownClass')

    def setUp(self):
        """
        Any code we want to run at the beginning of each test.
        """
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """
        Any code we want to run at the end of each test.
        """
        print('tearDown\n')

    ### TESTS ###

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')    

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')
    
    def test_fullname_setter(self):
        print('test_fullname_setter')

        self.emp_1.fullname = 'Jane Smith'
        self.emp_2.fullname = 'John Schafer'

        self.assertEqual(self.emp_1.fullname,'Jane Smith')
        self.assertEqual(self.emp_2.fullname, 'John Schafer')
    
    def test_fullname_deleter(self):
        print('test_fullname_deleter')

        del self.emp_1.fullname
        del self.emp_2.fullname

        self.assertEqual(self.emp_1.fullname, 'None None') 
        self.assertEqual(self.emp_2.fullname, 'None None') 

    def test_apply_raise(self):
        print('test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """
        Because this function depends on output of a get request, we don't want
        the test to fail if the website is down (or any reason other than 
        our code being broken). Thus, we use the patch function as a context
        manager to generate a mocked result from the get request.
        """
        with patch('src.employee.requests.get') as mocked_get:

            ### TRUE CASE ###

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            ### FALSE CASE ###

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
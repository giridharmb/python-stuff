import unittest
import requests
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee("Danny", "Choi", 100)
        self.emp_2 = Employee("Aaron", "Lanoy", 300)
    
    def tearDown(self):
        pass
    
    def test_01_email(self):
        self.assertEqual(self.emp_1.email, 'Danny.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Aaron.Lanoy@email.com')
        
    def test_02_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Danny Choi')
        self.assertEqual(self.emp_2.fullname, 'Aaron Lanoy')
        
    def test_03_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 200) 
        self.assertEqual(self.emp_2.pay, 600)
        
if __name__ == "__main__":
    unittest.main()

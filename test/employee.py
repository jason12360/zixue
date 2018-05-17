import unittest
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = int(salary)
    def give_raise(self,n = 5000):
        self.salary += n
        return self.salary

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('sary','1500')
        

    def test_give_default_raise(self):
        salary = self.my_employee.give_raise()
        self.assertEquals(salary,6500)
    def test_give_costum_raise(self):
        salary = self.my_employee.give_raise(3000)
        self.assertEqual(salary,4500)

unittest.main()

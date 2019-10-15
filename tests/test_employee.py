import unittest
from datetime import date

from employee_class import Employee


class TestsEmployeeClass(unittest.TestCase):

    def testCreatWithNoAtributes(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1))
        self.assertIsInstance(employee, Employee)

    def testCreatAllAtributes(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1),
                            position='student', experience=1, salary=500)
        self.assertIsInstance(employee, Employee)

    def testExpirienceLess0(self):
        with self.assertRaises(ValueError):
            employee = Employee('Ivan Ivanov', date(1901, 1, 1), experience=-1)

    def testSalaryLess0(self):
        with self.assertRaises(ValueError):
            employee = Employee('Ivan Ivanov', date(1901, 1, 1), salary=-1)

    def testFullPosition(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), position='student', experience=1)
        self.assertEqual('Junior student', employee.full_position())
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), position='student', experience=4)
        self.assertEqual('Middle student', employee.full_position())
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), position='student', experience=7)
        self.assertEqual('Senior student', employee.full_position())

    def testChangeSalary(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), salary=100)
        employee.change_salary(100)
        self.assertEqual(200, employee.salary)

    def testChangeSalaryMinus(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), salary=100)
        employee.change_salary(-100)
        self.assertEqual(0, employee.salary)

    def testChangeSalaryLessZero(self):
        employee = Employee('Ivan Ivanov', date(1901, 1, 1), salary=100)
        with self.assertRaises(ValueError):
            employee.change_salary(-200)

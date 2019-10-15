import unittest
from datetime import date, datetime

from person_class import Person


class TestsPersonClass(unittest.TestCase):

    def testEmptyAtributFullName(self):
        with self.assertRaises(ValueError):
            Person(birth_date=date(1902, 1, 1))

    def testAtributFullNameOneWord(self):
        with self.assertRaises(ValueError):
            Person(full_name='Ivanov Ivan')

    def testAtributFullNameThreeWord(self):
        with self.assertRaises(ValueError):
            Person(full_name='Ivanov Ivan Ivanovich')

    def testAtributFullNameDigits(self):
        with self.assertRaises(ValueError):
            Person(full_name='333 666', birth_date=date(1902, 1, 1))

    def testAtributBirthDateEmpty(self):
        with self.assertRaises(ValueError):
            Person(full_name='Ivanov Ivan')

    def testAtributBirthDateNotDate(self):
        with self.assertRaises(AttributeError):
            Person(full_name='Ivanov Ivan', birth_date=1)

    def testGetName(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        self.assertEqual('Ivan', person.get_name())

    def testGetSurname(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        self.assertEqual('Ivanov', person.get_surname())

    def testAgeIn(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        self.assertEqual(1, person.age_in(1902))

    def testAgeInStr(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            person.age_in('a')

    def testAgeInFloat(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            person.age_in(1.25)

    def testAgeInYearLessBirth(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            person.age_in(1900)

    def testAgeInYearMinus(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            person.age_in(-1900)

    def testAgeInYearNoParam(self):
        person = Person('Ivan Ivanov', date(1901, 1, 1))
        res = person.age_in()
        expect = datetime.now().year - 1901
        self.assertEqual(res, expect)

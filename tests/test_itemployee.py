import unittest
from datetime import date, datetime

from itemployee_class import ITEmployee


class TestsITEmployeeClass(unittest.TestCase):

    def testCreatWithNoAtributes(self):
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        self.assertIsInstance(itemployee, ITEmployee)

    def testCreateWithSkills(self):
        skills = ['Java', 'Python', 'C#']
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1), skills=skills)
        self.assertIsInstance(itemployee, ITEmployee)
        self.assertEqual(skills, itemployee.skills)

    def testAddSkillEmpty(self):
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            itemployee.add_skill()

    def testAddSkill(self):
        skills = ['Java', 'Python', 'C#']
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        for skill in skills:
            itemployee.add_skill(skill)
            self.assertEqual(skills[:skills.index(skill)+1], itemployee.skills)

    def testAddSkillsEmpry(self):
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        with self.assertRaises(ValueError):
            itemployee.add_skill()

    def testAddSkills(self):
        skills = ['Java', 'Python', 'C#']
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        itemployee.add_skills(*skills)
        self.assertEqual(skills, itemployee.skills)

    def testAddSkillsWithEmpty(self):
        skills = ['Java', 'Python', 'C#']
        skills2 = ['Java', '', 'Python', '', 'C#', '']
        itemployee = ITEmployee('Ivan Ivanov', date(1901, 1, 1))
        itemployee.add_skills(*skills2)
        self.assertEqual(skills, itemployee.skills)
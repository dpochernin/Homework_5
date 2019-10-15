from datetime import datetime, date
from employee_class import Employee

# ITEmployee (наследуемся от Employee)
# 1. Реализовать метод добавления одного навыка в новое свойство skills (список)
# новым методом add_skill (см. презентацию).
# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
# или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill


class ITEmployee(Employee):
    """full_name= str must be two words name and surname like 'Ivan Durak', raise ValueError if not\n
            birth_date= datetime.datetime.date obj , year must be in range 1900<year<current_year,
            raise ValueError if not\n
            position='' position str\n
            experience=0 years of experience int raise ValueError if <0\n
            salary=0 current salary of employee int raise ValueError if <0\n
            skills=[] skills of person default empty"""

    def __init__(self, full_name='', birth_date=date(datetime.now().year, datetime.now().month, datetime.now().day),
                 position='', experience=0, salary=0, skills=None):
        super().__init__(full_name, birth_date, position, experience, salary)
        if skills is None:
            skills = []
        self.skills = skills

    def add_skill(self, skill=''):
        if skill:
            self.skills.append(skill)
        else: raise ValueError(f'You add empty skill')

    def add_skills(self, *args):
        if args:
            for arg in args:
                try:
                    self.add_skill(arg)
                except ValueError: pass
        else: raise ValueError(f'You add empty skill')

    def __str__(self):
        return f'{super().__str__()}, {self.skills}'


if __name__ == '__main__':
    per = ITEmployee('Ivan Durak', date(1985, 10, 27), 'programmer', 5, 2500, ['Java', 'Python', 'C#'])
    print(per)

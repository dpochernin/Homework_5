from datetime import datetime, date
from person_class import Person

# Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
# ** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
# Реализовать новые методы:
# возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет,
# Senior — больше 6 лет.
# Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>.
# Если, например у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
# метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.


class Employee(Person):
    """full_name= str must be two words name and surname like 'Ivan Durak', raise ValueError if not\n
        birth_date= datetime.datetime.date obj , year must be in range 1900<year<current_year,
        raise ValueError if not\n
        position='' position str\n
        experience=0 years of experience int raise ValueError if <0\n
        salary=0 current salary of employee int raise ValueError if <0"""

    def __init__(self, full_name='', birth_date=date(datetime.now().year, datetime.now().month, datetime.now().day),
                 position='', experience=0, salary=0):
        super().__init__(full_name, birth_date)
        self._position = position
        if experience >= 0:
            self.experience = experience
        else:
            raise ValueError(f'experience={experience} can not be less 0')
        if salary >= 0:
            self.salary = salary
        else:
            raise ValueError(f'experience={salary} can not be less 0')

    def full_position(self) -> str:
        """return str of full position based on experience and position\n
        0..2 Junior; 3..6 Middle; 6 and more Senior"""
        status = ("Junior" if self.experience < 3 else
                  "Middle" if 3 <= self.experience < 6 else
                  "Senior")
        return f'{status} {self._position}'

    def change_salary(self, delta=0):
        """change salary of employee to delta\n
        delta=0 must be int, can be minus
        but
        delta in minus can not be more salary raise ValueError
        """
        if self.salary + delta >= 0:
            self.salary += delta
        else:
            raise ValueError(f'delta={delta} , sum of salary={self.salary} and delta can\'t be less 0')

    def __str__(self):
        return f'{super().__str__()}, {self._position}, {self.experience}, {self.salary}'


if __name__ == '__main__':
    per = Employee('Ivan Durak', date(1985, 10, 27), 'programmer', 5, 2500)
    print(per)

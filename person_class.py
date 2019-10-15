from datetime import datetime, date

# Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка
# и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
# Реализовать методы, которые:
# выделяет только имя из full_name
# выделяет только фамилию из full_name;
# вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year));
# если не передавать параметр, по умолчанию, сколько лет в этом году;
# ** (только для продвинутых) Можете в конструкторе проверить, что в full_name передаётся строка,
#    состоящая из двух слов, если нет, вызывайте исключение 😊
# ** (только для продвинутых) Можете в конструкторе проверить, что в год рождения меньше 2019,
#    но больше 1900, если нет вызывайте исключение


class Person:
    def __init__(self, full_name='', birth_date=date(1900, 1, 1)):
        """full_name= str must be two words name and surname like 'Ivan Durak', raise ValueError if not\n
           birth_date= datetime.datetime.date obj , year must be in range 1900<year<current_year,
           raise ValueError if not"""

        if len(full_name.split()) == 2:
            self._full_name = full_name
        else:
            raise ValueError(f'full_name="{full_name}" must be two words name and surname like "Ivan Durak"')
        if 1900 < birth_date.year < datetime.now().year:
            self._birth_date = birth_date
        else:
            raise ValueError(f'birth_date.year="{birth_date.year}" year must be in range 1900<year<current_year')

    def get_name(self) -> str:
        """return Name str as part of full_name"""
        return self._full_name.split()[0]

    def get_surname(self) -> str:
        """return Surname str as part of full_name"""
        return self._full_name.split()[1]

    def age_in(self, year=datetime.now().year) -> int:
        """return age of person based on birth_date and year\n
        year default is current year"""
        return year - self._birth_date.year

    def __str__(self):
        return f'{self._full_name}, {self._birth_date.strftime("%d.%m.%Y")}'


if __name__ == '__main__':
    per = Person('Ivan Durak', date(1985, 10, 27))
    print(per)
    print(per.get_surname())
    print(per.get_name())
    print(per.age_in(2019))

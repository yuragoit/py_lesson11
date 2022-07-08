from collections import UserDict
from datetime import time, datetime
from dateutil import parser
import time


class Record():

    def __init__(self, name, birthday=None, *args):
        self.name = Name(name).value
        self.birthday = Birthday(birthday).value
        self.phone = Phone(args).value

    def add_phone(self, key, *args):
        tmp = self.data[key][-1]
        tmp += Phone(args).value
        return self.data[key]

    def edit_phone(self, key, number, new_number):
        tmp = self.data[key][-1]
        while number in tmp:
            idx = tmp.index(number)
            tmp[idx] = new_number
        return self.data[key]

    def del_phone(self, key, number):
        tmp = self.data[key][-1]
        while number in tmp:
            idx = tmp.index(number)
            tmp.pop(idx)
        return self.data[key]

    def days_to_birthday(self, name):
        target = (self.data[name][0])
        # if type(target) is datetime:
        if isinstance(target, datetime):
            today = datetime.now()
            b_day = target.replace(year=today.year)
            delta = (b_day - today).days
            diff = delta if b_day >= today else delta + 365
            return f'For {name} rests {diff} days to the next birthday'
        else:
            return f'Please enter birthday date for customer {name}'


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__value = value
        else:
            print("Please enter a valid Name")
        return self.__value


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        arr = []
        for elem in value:
            if isinstance(elem, int) and len(str(elem)) == 12:
                arr.append(elem)
            elif not isinstance(elem, int):
                print(f"For phone number {elem} type of data must be int")
            elif len(str(elem)) != 12:
                print(
                    f"For phone number {elem} length must be equal 12 symbols")

        self.__value = arr
        return self.__value


class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            if value and isinstance(value, str) and len(value) < 12:
                self.__value = parser.parse(value)
            elif not value:
                self.__value = None
            else:
                print("Please enter a valid value")

        except:
            print("Enter valid data with format 'yyyymmdd'")
            self.__value = parser.parse(input())
        return self.__value


class AddressBook(UserDict, Record):

    def add_record(self, name, b_day=None, *args):
        record = Record(name, b_day, *args)
        self.data[record.name] = record.birthday, record.phone
        return self.data

    def get_phones(self, *name):
        for elem in name:
            if elem:
                rez = self.data[elem]
                print(f"For {elem} matched phones: {rez}")

    def iterator(self, N):
        iter_count = 0
        for i, key in enumerate(self.data.items()):
            print(key)
            if (i + 1) % N == 0:
                iter_count += 1
                # print("_"*32)
                # input("Press any key to continue output")
                print(f'Iteration number {iter_count}')
                time.sleep(2)


# Test working conditions for developed classes (pagination)
a = AddressBook()
# a.add_record("Alex", 1001)
a.add_record("Bils", "20010130", 380665214700)
a.add_phone("Bils", 380665214701)
a.add_record("Corsa", "20020429", 380505214701, 380665214702, 380666666666)
a.edit_phone("Bils", 380665214700, 380660000000)
a.del_phone("Corsa", 380666666666)
a.add_record("Darlin", '', 380665214703)
a.add_record("Egor", "", 380665214704)
a.add_record("Fedor", 0, 380665214705)
a.add_record("Georg", None, 380665214706, 380665214707)
a.add_record("Helda", None, 380665214708)
a.add_record("Izya", None, 380665214709)
a.add_record("John", None, 380665214710)
a.add_record("Katrin", None, 380665214711, 38000)
a.add_record("Levin", None, 380665214712, 380665214713)
a.iterator(3)
print(a.days_to_birthday("Bils"))
print(a.days_to_birthday("Corsa"))

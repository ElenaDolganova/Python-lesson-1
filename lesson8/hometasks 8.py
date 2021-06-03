# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    @staticmethod
    def valid(day, month, year):
        if 0 >= month > 12 or 0 >= day:
            return False

        max_possible_day = 31
        if month == 2:
            if year % 4 == 0:
                max_possible_day = 29
            else:
                max_possible_day = 28
        elif month in (4, 6, 7, 9, 11):
            max_possible_day = 30

        if day > max_possible_day:
            return False

        return True

    @classmethod
    def extract(cls, date):
        day, month, year = date.split('-')
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            raise Exception('not a valid date')

        if not cls.valid(day, month, year):
            raise Exception('not a valid date')

        return day, month, year

    def __init__(self, date):
        self.day, self.month, self.year = self.extract(date)


d = Date('14-02-2021')
print(d.day, d.month, d.year)
d = Date('14-12-2021')
print(d.day, d.month, d.year)
d = Date('14-12-21')
print(d.day, d.month, d.year)

try:
    d = Date('41-12-21')
except Exception as ex:
    print(ex)

try:
    d = Date('aa-bb-cccc')
except Exception as ex:
    print(ex)


try:
    d = Date('29-02-1993')
except Exception as ex:
    print(ex)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


a = int(input('Enter first: '))
b = int(input('Enter second: '))
try:
    print('result is: ', a / b)
except ZeroDivisionError:
    print('Division by zero is not possible')


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере.
#  Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить
# его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

result_list = []
user_data = None
while user_data != 'stop':
    user_data = input('Enter number: ')
    try:
        user_data = int(user_data)
    except ValueError:
        print('not a number')
        continue
    result_list.append(user_data)

print('Result list:', result_list)

# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Storage:
    pass


class OfficeItem:
    pass


class Printer(OfficeItem):
    def __init__(self):
        self.color = True


class Scanner(OfficeItem):
    def __init__(self):
        self.has_wifi = True


class Xerox(OfficeItem):
    def __init__(self):
        self.broken = True


# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.


class Storage:
    _storage = {'storage': []}

    def accept(self, item):
        self._storage['storage'].append(item)

    def _move_to_department(self, department_name, item):
        self._storage['storage'].remove(item)
        if department_name in self._storage:
            self._storage[department_name].append(item)
        else:
            self._storage[department_name] = [item]

    def provide(self, department_name, item_type):
        for item in self._storage['storage']:
            if type(item) == item_type:
                self._move_to_department(department_name, item)
                return

        raise Exception('item type not present')

    def status(self):
        return self._storage


class OfficeItem:
    pass


class Printer(OfficeItem):
    def __repr__(self):
        return f'Printer <{"color" if self.color else "black"}>'

    def __init__(self, color):
        self.color = color


class Scanner(OfficeItem):
    def __repr__(self):
        return f'Scanner <{"with wifi" if self.has_wifi else "with cable"}>'

    def __init__(self, has_wifi):
        self.has_wifi = has_wifi


class Xerox(OfficeItem):
    def __repr__(self):
        return f'Scanner <{"broken" if self.broken else "repaired"}>'

    def __init__(self, broken):
        self.broken = broken


# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


types_dict = {'xerox': Xerox, 'printer': Printer, 'scanner': Scanner}

def parse_type_and_count(item_type, item_count):
    try:
        item_type = types_dict[item_type]
    except KeyError:
        print('Item type is wrong')
        raise
    try:
        item_count = int(item_count)
    except ValueError:
        print('Item count is not a number')
        raise

    return item_type, item_count


storage = Storage()
user_input = None
while True:
    user_input = input('Input command: ')
    if user_input == 'stop':
        break
    elif user_input == 'status':
        print(storage.status())
        continue
    elif user_input.startswith('add'):
        try:
            _, item_type, item_count = user_input.split()
        except:
            print('Wrong syntax. Correct: "add type count"')
            continue

        try:
            item_type, item_count = parse_type_and_count(item_type, item_count)
        except:
            continue

        for i in range(item_count):
            storage.accept(item_type(i % 2))

    elif user_input.startswith('provide'):
        try:
            _, item_type, item_count, department_name = user_input.split()
        except:
            print('Wrong syntax. Correct: "provide type count department_name"')
            continue

        try:
            item_type, item_count = parse_type_and_count(item_type, item_count)
        except:
            continue

        try:
            for _ in range(item_count):
                storage.provide(department_name, item_type)
        except:
            print(item_count)
            print('Not enough items to provide')
            continue
    else:
        print('Wrong command. Try "add", "provide", "status"')

# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __str__(self):
        return f'{self.real} {self.imaginary}i'

a = ComplexNumber(2, 3)
b = ComplexNumber(-1, 1)
print(a + b)
print(a * b)
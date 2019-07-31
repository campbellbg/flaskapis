'''
my_set = {10, 20, 40, 40}
my_set1 = {40, 30, 20}

print(my_set.intersection(my_set1))
print(my_set.difference(my_set1))
print(my_set1.difference(my_set))
print(my_set1.union(my_set))
'''

'''

for my_char in 'hello there':
    print(my_char)

my_list = range(1, 5)

for i in my_list:
    print(i)

while i < 5:
    print(i)
    i = i + 1

def multiply_me(x, y):
    if y <= 0:
        return 1
    else:
        return x * y


print(multiply_me(1, 0))
print(multiply_me(1, 2))

'''

'''
import pandas as pd

def even_only(the_list):

    new_list = []

    for i in the_list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

play_list = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], columns=['A'])

print(play_list[play_list['A'] % 2 == 0])
'''

'''

my_students = [{'name':'bryan', 'grades':(20, 30, 40)}, {'name':'kate', 'grades':(10, 30, 90)}]


def get_average_grade(student):
    return sum(student['grades']) / len(student['grades'])

def get_total_average_grade(students):

    all_grades = ()

    for i in students:
        all_grades += i['grades']

    return (sum(all_grades) / len(all_grades))


print(get_average_grade(my_students[1]))
print(get_total_average_grade(my_students))

'''

'''
class Lottery_Player:
    def __init__(self):
        self.__name = 'Bryan'
        self.__numbers = {1, 2, 3, 4, 5}

    def __getattr__(self, item):
        return self.__name + 'Hello'

a = Lottery_Player()
b = Lottery_Player()

print(a.name)

'''
'''
class Student:

    def __init__(self):
        pass

    def instance_respond(self):
        print('Hi from the object')

    @staticmethod
    def respond():
        print('Hi There from the static')

    @classmethod
    def respond1(cls):
        print(f'Hi there from {cls.__name__}')


a = Student()
a.instance_respond()
a.respond()
a.respond1()

'''

'''

class Franchise:

    cnt = 0

    def __init__(self):
        self.store_list = []


    def get_stores(self):
        for i, x in enumerate(self.store_list):
            print(f'Store {i + 1}: {x.store_name}')


    def new_store(self, store):
        self.store_list.append(store)
        Franchise.enumerate_cnt()

    @classmethod
    def enumerate_cnt(cls):
        cls.cnt += 1

    @classmethod
    def get_cnt(cls):
        cls.cnt += 1

class Store:

    def __init__(self, name):
        self.store_name = name

f = Franchise()
s1 = Store('Coles')
s2 = Store('WW')

print(Franchise.cnt)

f.new_store(s1)
f.new_store(s2)

print(Franchise.cnt)

f.get_stores()

'''

'''
#Student & Working Student working example

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def friend(self, friend_name):
        return WorkingStudent(friend_name, self.school, 5)

    def add_result(self, result):
        self.marks.append(result)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def take_test(self):
        super().add_result(10)

student_1 = WorkingStudent('Bryan', 'Eltham', 10)
student_2 = student_1.friend('Kate')

print(f'{student_1.name} attends {student_1.school}')
print(f'{student_2.name} attends {student_2.school}')
student_1.add_result(20)
student_1.take_test()
print(student_1.marks)

'''

'''
def my_func(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(list(filter(lambda x: x%2 ==0, [1,2,3,4])))

print((lambda x, y: x + y)(2, 3))

print(list(map(lambda x: (x[0] + 1, x[1] + 2), [(1,2), (3,4)])))

'''
'''
import functools

def my_decorator(f):
    @functools.wraps(f)
    def new_function(i):
        print(f'starting execution for parameter no: {i}')
        f(i)
        print(f'ending execution for parameter no: {i}')
    return new_function


@my_decorator
def test_function(i):
    print('middle of wrap')

test_function(1)

'''
'''

def dec_with_arg(x):
    def dec(my_func):
        def new_function(*args, **kwargs):
            if x == 99:
                print('Not running the function')
            else:
                my_func(*args, **kwargs)
        return new_function
    return dec


@dec_with_arg(100)
def norm_func(a, b):
    print(f'The normal function {a}, {b}')


norm_func(1, b = '2')

'''


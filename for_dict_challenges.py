
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = [student["first_name"] for student in students]
from collections import Counter
count_names = dict(Counter(names))
for key, value in count_names.items():
    print(f"{key}:{value}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [student["first_name"] for student in students]
from collections import Counter
count_names = dict(Counter(names))
import operator
name_repeat = max(count_names.items(), key=operator.itemgetter(1))[0]
print(f"Самое частое имя среди учеников: {name_repeat}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for i, group in enumerate(school_students,start=1):
    names = [student["first_name"] for student in group]
    count_names = dict(Counter(names))
    name_repeat = max(count_names.items(), key=operator.itemgetter(1))[0]
    print(f"Самое частое имя среди учеников в классе {i}: {name_repeat}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def get_students_names(students: list[dict[str,str]]) -> list[str]:
   return [student['first_name'] for student in students]

def count_boys_girls(group: list[str]) -> tuple[int, int]:
    count_boys = 0
    count_girls = 0
    for name in group:
        if is_male[name]:
            count_boys +=1
        else:
            count_girls +=1
    return count_boys,count_girls

def get_gender_in_school(school) -> None:
    for group in school:
        students_names = get_students_names(group['students'])
        boys,girls = count_boys_girls(students_names)
        print(f'Класс {group["class"]} мальчики: {boys}, девочки: {girls}')

get_gender_in_school(school)

# Класс 2б: девочки 0, мальчики 2

assert count_boys_girls(['Маша','Оля', 'Олег']) == (1,2)
assert count_boys_girls([]) == (0,0)
assert get_students_names([{'first_name': 'Маша'}, {'first_name': 'Оля'}]) == ['Маша','Оля']

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def get_students_names(students: list[dict[str,str]]) -> list[str]:
   return [student['first_name'] for student in students]

def count_boys_girls(group: list[str]) -> tuple[int, int]:
    count_boys = 0
    count_girls = 0
    for name in group:
        if is_male[name]:
            count_boys +=1
        else:
            count_girls +=1
    return count_boys,count_girls

def get_gender_in_school(school):
    gender_in_school = []
    for group in school:
        students_names = get_students_names(group['students'])
        boys,girls = count_boys_girls(students_names)
        gender_in_class = {"class" : group["class"], "boys": boys, "girls": girls}
        gender_in_school.append(gender_in_class)
    return gender_in_school

groups = get_gender_in_school(school)

def compare_boys_girls(groups: dict):
    i = 0
    if groups[i]["boys"] > groups[i+1]["boys"]:
        print(f"Больше мальчиков в классе {groups[i]['class']}")
    elif groups[i]["boys"] < groups[i+1]["boys"]:
        print(f"Больше мальчиков в классе {groups[1]['class']}")
    if groups[i]["girls"] > groups[i+1]["girls"]:
        print(f"Больше девочек в классе {groups[0]['class']}")
    elif groups[i]["girls"] < groups[i+1]["girls"]:
        print(f"Больше девочек в классе {groups[1]['class']}")

compare_boys_girls(groups)








# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import date, timedelta
today = date.today()
print(today)
yestarday = today - timedelta(days = 1)
print(yestarday)
#30 days before
other_date = today - timedelta(days=30)
print(other_date)

#РАБОТА С ФАЙЛАМИ

with open('referal.txt',"r", encoding= 'utf-8') as f:
    content = f.read()
    print(f"Длинна строки {len(content)} символов")
    print(f"Количество слов в строке {len(content.split())}")
    new_content = content.replace(".", "!")

with open('referal2.txt',"w", encoding= 'utf-8') as f:
    content = f.write(new_content)

#CSV
import csv
list_of_dict =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
keys = list_of_dict[0].keys()


with open ("customer.csv","w", newline= "") as file:
        dict_writer = csv.DictWriter(file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dict)




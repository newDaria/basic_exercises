# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "аеоуэиый":
           num_vowels = num_vowels+1
    return num_vowels
print(countvowels(word.lower()))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_split = sentence.split()
new_str_first_letters = ""
for i in sentence_split:
    new_str_first_letters += i[0]
print(new_str_first_letters)


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_split_list = sentence.split()
new_list = []
for i in sentence_split_list:
        new_list.append(len(i))
print(sum(new_list)/len(new_list))

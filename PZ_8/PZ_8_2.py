#Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод"
#английского слова на русский.

english_word = {
    'hello': 'привет',
    'bye': 'пока',
    'yes': 'да',
    'no': 'нет',
    'thank you': 'спасибо',
    'please': 'пожалуйста',
    'sure': 'конечно',
    'sorry': 'прости',
    'hope': 'надежда',
    'love': 'любовь',
}

def translate(word):
   return english_word.get(word)

w = input('Введите слово на английском: ')
print(translate(w))
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

more_words = 0
three_words = 0
two_words = 0
one_word = 0

for query in queries:
    if len(query.split()) == 3:
        three_words += 1
    elif len(query.split()) == 2:
        two_words += 1
    elif len(query.split()) == 1:
        one_word += 1
    else:
        more_words += 1

percentage_three = round(three_words * 100 / len(queries))
print(f'one word - {round(one_word * 100 / len(queries))} %')
print(f'two words - {round(two_words * 100 / len(queries))} %')
print(f'three_words - {percentage_three} %')
print(f'more words - {round(more_words * 100 / len(queries))} %')

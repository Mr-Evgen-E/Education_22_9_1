import random

while True:
    try:
        seq_numbers = list(map(int, (input("Введите последовательность целых чисел через пробел: ").split())))
        any_number = int(input("Введите любое целое число из последовательности: "))
        break

    except ValueError:
        print("Ошибка! Введите число. Повторите ввод заново.")

left = 0
right = int(len(seq_numbers) - 1)


# Сортировка последовательности
def qsort_random(seq_numbers_func, left_func, right_func):
    p = random.choice(seq_numbers_func[left_func:right_func + 1])
    i, j = left_func, right_func
    while i <= j:
        while seq_numbers_func[i] < p:
            i += 1
        while seq_numbers_func[j] > p:
            j -= 1
        if i <= j:
            seq_numbers_func[i], seq_numbers_func[j] = seq_numbers_func[j], seq_numbers_func[i]
            i += 1
            j -= 1

    if j > left_func:
        qsort_random(seq_numbers_func, left_func, j)
    if right_func > i:
        qsort_random(seq_numbers_func, i, right_func)

    return seq_numbers_func


sort_numbers = qsort_random(seq_numbers, left, right)
print("Результат сортировки:", ' '.join(map(str, sort_numbers)))


# Поиск индекса введенного числа
def binary_search(sort_numbers_func, any_number_func, left_func, right_func):
    if left_func > right_func:
        return False

    middle = (right_func + left_func) // 2
    if sort_numbers_func[middle] == any_number_func:
        return middle
    elif any_number_func < sort_numbers_func[middle]:
        return binary_search(sort_numbers_func, any_number_func, left_func, middle - 1)
    else:
        return binary_search(sort_numbers_func, any_number_func, middle + 1, right_func)


search_result = binary_search(sort_numbers, any_number, left, right)

# Ищем первое число в повторяющихся числах и записываем его Индекс в результат поиска
while sort_numbers[search_result] == sort_numbers[search_result - 1]:
    search_result = search_result - 1

# Устанавливаем индексы предыдущего числа и следующего за нашим
previous_index = search_result - 1
next_index = search_result + 1

# Вывод результатов поиска
if search_result or type(search_result) is int:
    print("Результат поиска, индекс числа:", search_result, "Его номер по счету:", search_result + 1)

    if previous_index < 0:
        print("Ваше число первое в последовательности, предыдущего индекса нет")
    else:
        print("Индекс предыдущего числа:", previous_index, "Его номер по счету:", previous_index + 1)

    if next_index > len(seq_numbers) - 1:
        print("Ваше число последнее в последовательности, следующего индекса нет")
    else:
        print("Индекс следующего числа:", next_index, "Его номер по счету:", next_index + 1)
else:
    print("Вашего числа нет в последовательности. Введите число из последовательности.")

1
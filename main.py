import random

while True:
    try:
        seq_numbers = list(map(int, (input("Введите последовательность целых чисел через пробел: ").split())))
        any_number = int(input("Введите любое целое число из последовательности: "))
        break
    except:
        print("Ошибка! Введите число. Повторите ввод заново.")

left = 0
right = int(len(seq_numbers) - 1)

# Сортировка последовательности
def qsort_random(seq_numbers, left, right):
    p = random.choice(seq_numbers[left:right + 1])
    i, j = left, right
    while i <= j:
        while seq_numbers[i] < p:
            i += 1
        while seq_numbers[j] > p:
            j -= 1
        if i <= j:
            seq_numbers[i], seq_numbers[j] = seq_numbers[j], seq_numbers[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(seq_numbers, left, j)
    if right > i:
        qsort_random(seq_numbers, i, right)

    return seq_numbers


sort_numbers = qsort_random(seq_numbers, left, right)
print("Результат сортировки:", ' '.join(map(str, sort_numbers)))

# Поиск индекса введенного числа
def binary_search(sort_numbers, any_number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sort_numbers[middle] == any_number:
        return middle
    elif any_number < sort_numbers[middle]:
        return binary_search(sort_numbers, any_number, left, middle - 1)
    else:
        return binary_search(sort_numbers, any_number, middle + 1, right)

search_result = binary_search(sort_numbers, any_number, left, right)

# Ищем первое число в повторяющихся числах и записываем его Индекс в результат поиска
while sort_numbers[search_result] == sort_numbers[search_result - 1]:
    search_result = search_result - 1

# Устанавливаем индексы предущего числа и следующего за нашим
previous_index = search_result - 1
next_index = search_result + 1

# Вывод результатов поиска
if search_result != False or type(search_result) is int:
    print("Результат поиска, индекс числа:", search_result, "Его номер по счету:", search_result + 1)

    if previous_index < 0:
        print("Ваше число первое в последовательности, предыдщего индекса нет")
    else:
        print("Индекс предыдущего числа:", previous_index, "Его номер по счету:", previous_index + 1)

    if next_index > len(seq_numbers) - 1:
        print("Ваше число последнее в последовательности, следующего индекса нет")
    else:
        print("Индекс следующего числа:", next_index, "Его номер по счету:", next_index + 1)

else:
    print("Вашего числа нет в последовательности. Введите число из последовательности.")

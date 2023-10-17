def list(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        MinNum = min(even_numbers)
    else:
        MinNum = numbers[0]
    numbers.sort(key=lambda x: (x == 0, x))
    return MinNum, numbers


lst = [int(num) for num in input("Введите числа через пробел: ").split()]
MinNum, nlst = list(lst)
if MinNum % 2 != 0:
    print("Четных элементов нет. Первый элемент списка:", MinNum)
else:
    print("Наименьший четный элемент:", MinNum)
print("Преобразованный список:", nlst)
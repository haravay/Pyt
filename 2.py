def bank(a, years):
    balance = a
    for _ in range(years):
        balance += balance * 0.1
    return balance

def elements(data):
    if isinstance(data, set):
        return sum(data)
    elif isinstance(data, str):
        if "[" in data and "]" in data:
            data = data.replace("[", "").replace("]","")
            data = [int(num) for num in data.split(",")]
            if len(data) >= 2:
                negatives = [num for num in data if num < 0]
                if len(negatives) >= 2:
                    product = negatives[0] * negatives[1]
                    print("Произведение первых двух отрицательных элементов:", product)
            if len(data) >= 2:
                min_index = data.index(min(data))
                max_index = data.index(max(data))
                data[min_index], data[max_index] = data[max_index], data[min_index]
        else:
            if " " in data:
                numbers = [int(num) for num in data.split()]
                return sum(numbers)

            else:
                words = data.split()
                if any(char.isdigit() for char in data):
                    max_word = max(words, key=len)
                    data= max_word
                else:
                    longest_word = max(words, key=len)
                    return longest_word
            return data

def sum_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    column_sums = [sum(matrix[row][col] for row in range(num_rows)) for col in range(num_cols)]
    return column_sums

while True:
    print("Меню:")
    print("1. Задание 1")
    print("2. Задание 2")
    print("3. Задание 3")
    print("4. Задание 4")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        while True:
            try:
                a = float(input("Введите размер вклада: "))
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Попробуйте снова.")


        while True:
            try:
                years = int(input("Введите количество лет: "))
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Попробуйте снова.")

        final_balance = bank(a, years)
        print("Сумма на счету после", years, "лет:", final_balance)

    elif choice == "2":
        data = input("Введите аргументы (через пробел или в формате [1, 2, 3]): ")
        if data.isdigit():
            number = int(data)
            print("Результат:", sum(int(digit) for digit in str(data)))
            continue
        if not any(char.isdigit() for char in data):
            words = data.split()
            longest_word = max(words, key=len)
            print("Результат:", longest_word)
            continue
        result = elements(data)
        print("Результат:", result)

    elif choice == "3":
        while True:
            try:
                m = int(input("Введите количество строк матрицы (не менее 1): "))
                if m < 1:
                    raise ValueError
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Количестов строк должно быть не менее 1. Попробуйте снова.")

        while True:
            try:
                n = int(input("Введите количество столбцов матрицы (не менее 1): "))
                if n < 1:
                    raise ValueError
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Количество столбцов должно быть не менее 1. Попробуйте снова.")

        matrix = []
        for _ in range(m):
            while True:
                try:
                    row = [int(num) for num in input("Введите элементы строки через пробел: ").split()]
                    if len(row) !=n:
                        raise ValueError
                    break
                except ValueError:
                    print("Ошибка: Введено некорректное значение. Попробуйте снова.")

            matrix.append(row)

        column_sums = sum_columns(matrix)
        print("Суммы столбцов матрицы: ", column_sums)

    elif choice == "4":
        while True:
            try:
                num1 = int(input("Введите первое число: "))
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Попробуйте снова.")

        while True:
            try:
                num2 = int(input("Введите второе число: "))
                if num2 == 0:
                    raise ZeroDivisionError
                break
            except ValueError:
                print("Ошибка: Введено некорректное значение. Попробуйте снова.")
            except ZeroDivisionError:
                print("Ошибка: Деление на ноль")

        try:
            result = num1 / num2
            print("Результат деления: ", result)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")
        finally:
            print("Выполнение блока finally")

    elif choice == "0":
        break
    else:
        print("Некоректный выбор")
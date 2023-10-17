toys = {
        'Мяч': {'описание': 'Красный мяч', 'цена': 10, 'количество': 5},
        'Кубики': {'описание': 'Набор ярких кубиков', 'цена': 15, 'количество': 3},
        'Кукла': {'описание': 'Пластиковая кукла', 'цена': 20, 'количество': 2},
        'Машинка': {'описание': 'Металлическая машинка', 'цена': 12, 'количество': 7}
    }

def descr():
    print("Описание игрушек:")
    for toy, details in toys.items():
        print(f"{toy} – {details['описание']}")

def price():
    print("Цены на игрушки:")
    for toy, details in toys.items():
        print(f"{toy} – {details['цена']}")

def colvo():
    print("Количество игрушек:")
    for toy, details in toys.items():
        print(f"{toy} – {details['количество']}")

def info():
    print("Информация об игрушках:")
    for toy, details in toys.items():
        print(f"Название: {toy}")
        print(f"Описание: {details['описание']}")
        print(f"Цена: {details['цена']}")
        print(f"Количество: {details['количество']}")
        print()

def buy():
    TPrice = 0
    while True:
        TName = input("Введите название игрушки (или 'n' для выхода): ")
        if TName == 'n':
            break
        if TName not in toys:
            print("Такой игрушки нет в магазине.")
            continue
        nColvo = input("Введите количество: ")
        if not nColvo.isdigit():
            print("Некорректное количество.")
            continue
        nColvo = int(nColvo)
        if nColvo > toys[TName]['количество']:
            print("Недостаточное количество игрушек.")
            continue
        price = toys[TName]['цена'] * nColvo
        TPrice += price
        toys[TName]['количество'] -= nColvo
        print(f"Покупка игрушки '{TName}' в количестве {nColvo} шт. выполнена успешно.")
    print(f"Общая стоимость покупок: {TPrice}")
    print("Остаток в магазине:")
    colvo()

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")
    ch = input("Выберите пункт меню: ")

    if ch == '1':
        descr()
    elif ch == '2':
         price()
    elif ch == '3':
        colvo()
    elif ch == '4':
        info()
    elif ch == '5':
        buy()
    elif ch == '6':
        break
    else:
        print("Некорректный ввод")

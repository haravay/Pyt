with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    if len(lines) < 10:
        print("Недостаточно строк в файле")
    else:
        for line in lines:
            name, price = line.split()
            price = float(price)
            if price >= 10:
                print(name, price)
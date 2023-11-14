def Maxi(num):
    max_digit = 0
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    return max_digit


while True:
    number = input("Введите число: ")
    if not number.isdigit():
        print("Некоректный ввод.")
        continue
    else:
        break



number = int(number)
max_digit = Maxi(number)
print("Максимальная цифра:", max_digit)

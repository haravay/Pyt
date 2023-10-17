def Maxi(num):
    max_digit = 0
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    return max_digit


number = int(input("Введите число: "))
max_digit = Maxi(number)
print("Максимальная цифра:", max_digit)

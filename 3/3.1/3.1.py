with open('text.txt', 'w', encoding='utf-8') as text:
    while True:
        line = input("Введите строку (Для окончания введите пустой символ)")
        if line == "":
            break
        text.write(line + "\n")
    text.seek(0)
with open('text.txt', 'r', encoding='utf-8') as text, open ('text2.txt', 'w', encoding='utf-8') as text2:
    lines = text.readlines()

    if len(lines) < 4:
        print("Недостаточно строк")
    else:
        text2.wrirelines(lines[3:])

with open('text2.txt', 'r', encoding='utf-8') as text2:

    lines = text2.readlines()
    if lines:
        lastLine = lines[-1]
        lastWord = lastline.split()[-1]
        ch = len(lastWord)
        print("Количество символов в последнем слове: ")
    else:
        print("Ошибка")
def remove(text):
    while '(' in text and ')' in text:
        text = text.replace('(', '').replace(')', '')
    return text


string = input("Введите строку с текстом в скобках: ")
new_string = remove(string)
print("Строка после удаления всех скобок:", new_string)
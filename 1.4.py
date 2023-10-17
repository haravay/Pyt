text = ' Follow your heart'
ch = {}
for char in text:
    if char in ch:
        ch[char] += 1
    else:
        ch[char] = 1

print("Словарь:")
for char, count in ch.items():
    print(f"{char}: {count}")
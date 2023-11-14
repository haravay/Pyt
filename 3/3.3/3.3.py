subjects = {}

with open('subjects.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    if len(lines) < 1:
        print("Пустой текстовый документ")
    else:
        for line in lines:
            subject, lessons = line.split(":")
            subject = subject.strip()
            alllessons = sum(int(lessons.split("(")[0]) for lesson in lessons.split())
            subjects[subject] = alllessons
        print(subjects)
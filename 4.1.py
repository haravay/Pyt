class Human:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        age = 2023 - self.birth_year
        print(f"Имя: {self.name}, Возраст: {age}")

    def is_adult(self):
        age = 2023 - self.birth_year
        if age >= 18:
            print(f"{self.name} является совершеннолетним")
        else:
            print(f"{self.name} несовершеннолетний")

person = Human("Иван", 1990)
person.display_info()
person.is_adult()
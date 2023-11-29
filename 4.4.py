class MyClass:
    class_attribute = 10

    def __init__(self, instance_attribute):
        self.instance_attrute = instance_attribute
    def instance_method(self):
        print("Это метод экземпляра")
    @staticmethod
    def static_method():
        print("Это статический метод")
    @classmethod
    def class_method(cls):
        print("Это метод класса")
        print("Значение class_attribute:", cls.class_attribute)

obj = MyClass(20)
print(obj.instance_attrute)
obj.instance_method()
MyClass.static_method()
MyClass.class_method()
print(MyClass.class_attribute)
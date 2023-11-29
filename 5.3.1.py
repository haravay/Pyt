import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 12.5, 0.5)
f_x = np.divide(1, np.tan(x)) ** 3 + 2.24 * x * 3.567
f_x = np.where(x != 0, f_x, 0)

for i in range(len(x)):
    print("a =", x[i], "f(x) =", f_x[i])

max_value = np.max(f_x)
min_value = np.min(f_x)
mean_value = np.mean(f_x)
num_elements = len(f_x)
if len(f_x) % 2 == 0:
    sorted_f_x = np.sort(f_x)[::-1]
else:
    sorted_f_x = np.sort(f_x)

plt.plot(x, f_x, 'bo-', label='f(x)')
plt.axhline(mean_value, color='r', linestyle='--', label='Mean')
plt.xlabel('a')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.legend()
plt.show()

print("Наибольшее значение функции:", max_value)
print("Наименьшее значение функции:", min_value)
print("Среднее значение функции:", mean_value)
print("Количество элементов в массиве:", num_elements)
print("Отсортированный массив:")
print(sorted_f_x)
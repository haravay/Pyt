import numpy as np

X = np.zeros((12, 3))
X[:, 0] = 1
X[:, 1] = np.arange(5, 17)
X[:, 2] = np.random.randint(60, 83, size=(12,))
Y = np.random.uniform(13.5, 18.6, size=(12, 1))
A = np.linalg.lstsq(X, Y, rcond=None)[0]
Y_predicted = X.dot(A)

print("Матрица X:")
print(X)
print("Вектор-столбец Y:")
print(Y)
print("Вектор оценок A:")
print(A)
print("Проверка: Предсказанный вектор Y:")
print(Y_predicted)
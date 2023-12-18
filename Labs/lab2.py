import numpy as np


def m(a, b):
    return 1 if a != b else 0


def get_leven(a, b):
    a = a.lower()
    b = b.lower()
    mas = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if min(i, j) == 0:
                mas[i][j] = max(i, j)
            else:
                mas[i][j] = min(mas[i - 1][j] + 1, mas[i][j - 1] + 1, mas[i - 1][j - 1] + m(a[i - 1], b[j - 1]))
    print(int(mas[-1][-1]))


def get_damery_leven(a, b):
    a = a.lower()
    b = b.lower()
    mas = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if min(i, j) == 0:
                mas[i][j] = max(i, j)
            elif i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                mas[i][j] = min(mas[i - 1][j] + 1, mas[i][j - 1] + 1, mas[i - 1][j - 1] + m(a[i - 1], b[j - 1]), mas[i - 2][j - 2] + 1)
            else:
                mas[i][j] = min(mas[i - 1][j] + 1, mas[i][j - 1] + 1, mas[i - 1][j - 1] + m(a[i - 1], b[j - 1]))
    print(int(mas[-1][-1]))


def main():
    a = input("Введите первое слово: ")
    b = input("Введите второе слово: ")
    print("Расстояние Левенштейна: ", end="")
    get_leven(a, b)
    print("Расстояние Дамер-Левенштейна: ", end="")
    get_damery_leven(a, b)


if __name__ == "__main__":
    main()

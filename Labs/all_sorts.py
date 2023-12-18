import random
import time


def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def bogoSort(a):
    st = time.time()
    n = len(a)
    while not is_sorted(a):
        random.shuffle(a)
        if time.time() - st > 60:
            print("Не получилось отсортировать")
            return


def bozosort(a):
    n = len(a)
    st = time.time()
    while not is_sorted(a):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        a[i], a[j] = a[j], a[i]
        if time.time() - st > 60:
            print("Не получилось отсортировать")
            return


def stoogesort(a, l, h):
    if l >= h:
        return
    if a[l] > a[h]:
        a[l], a[h] = a[h], a[l]
    if h - l + 1 > 2:
        t = int((h - l + 1) / 3)
        stoogesort(a, l, (h - t))
        stoogesort(a, l + t, h)
        stoogesort(a, l, h - t)


def selection_sort(a):
    n = len(a)
    for i in range(0, n):
        current_min = a[i]
        min_index = i
        for j in range(i, n):
            if a[j] < current_min:
                current_min = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


def bubble_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def transfer(n, x):
    result = []
    while n > 0:
        result.append(n % x)
        n //= x
    return result[::-1]


def babushkinsort(a):
    n = len(a)
    while not is_sorted(a):
        b = [0] * n
        x, y = 1, 1
        while x % y == 0:
            x = random.randint(1000000, 1000000000)
            y = random.randint(1000000, 1000000000)
        x, y = min(x, y), max(x, y)
        dec = int(str(x / y * 10).replace(".", ""))
        dec = transfer(dec, n)
        used = []
        for i in dec:
            if i not in used:
                used.append(i)
        if len(used) != len(dec):
            continue
        print(1)
        for i in range(n):
            b[dec[i]] = a[i]
        if is_sorted(b):
            a = b.copy()
            return


def use_sort(func, mas, name):
    list_to_sort = mas.copy()
    st = time.time()
    if func == stoogesort:
        func(list_to_sort, 0, len(mas) - 1)
    else:
        func(list_to_sort)
    print(f"{name}:\n time = {time.time() - st}\n original list: {mas}\n sorted list: {list_to_sort}")


def main(n, a, b):
    original_list = []
    print("N =", n, "A =", a, "B =", b)
    for i in range(n):
        original_list.append(random.randint(a, b))

    names = ["BogoSort", "BozoSort", "Stooge sort", "Selection sort", "Bubble sort"]
    funcs = [bogoSort, bozosort, stoogesort, selection_sort, bubble_sort]

    for i in range(len(names)):
        use_sort(funcs[i], original_list, names[i])


if __name__ == "__main__":
    for i in range(10, 120, 50):
        main(i, 0, i)
        main(i, 0, 3 * i)

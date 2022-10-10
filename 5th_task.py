# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

from random import randint

r = int(input('enter count of rows: '))
c = int(input('enter count of columns: '))


def create_mat(r, c):
    arr_2d = []

    for i in range(r):
        inner_arr = []

        for j in range(c):
            inner_arr.append(randint(0, 9))

        arr_2d.append(inner_arr)

    return arr_2d


def print_mat(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            print(arr_2d[i][j], end=' ')
        print()

def mat_sort(a):
    indexing_length = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if a[i] > a[i + 1]:
                sorted = False
                a[i], a[i + 1] = a[i + 1], a[i]

    return a

created_arr = create_mat(r, c)

print_mat(created_arr)
print()
print_mat(mat_sort(created_arr))
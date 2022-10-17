#1

"""list = [1, 6, 8, 5, 4, 0, 3], [5, 7, 8, 9, 4, 2, 1], [6, 0, 7, 8, 1, 2, 5], [5, 7, 2, 7, 5, 2, 1]
print('Многомерный список:')
for row in list:
    for number in row:
        print(number, end=' ')
    print()
print('Первый и последний столбец:')
for row in list:
    print(row[0], row[len(row) - 1])"""

#2
list = [1, 6, 8, 5, 4, 0, 3], [5, 7, 8, 9, 4, 2, 1], [6, 0, 7, 8, 1, 2, 5], [5, 7, 2, 7, 5, 2, 1]
print('Многомерный список:')
for row in list:
    for number in row:
        print(number, end=' ')
    print()
print('Четные столбцы с елементом больше последнего:')
for s in range(len(list)):
    print()
    for number in range(len(list[s])):
        if number % 2 == 0 and list[0][number] > list[-1][number]:
            print(list[s][number], end=' ')


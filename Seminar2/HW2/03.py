# Задайте список из n чисел, заполненный по формуле:
# (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input())
sum = 0
n_list = []

for i in range(1, n + 1):
    res = round((1 + 1/i) ** i, 3)
    n_list.append(res)
    sum += res

print(n_list)
print(sum)

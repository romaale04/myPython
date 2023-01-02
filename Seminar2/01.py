# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# 1, -3, 9, -27, 81

# n = int(input())

# for i in range (n):
#     print((-3)**i, end=' ')




n = int(input())
seq_n = 1

for i in range (n):
    print(seq_n, end=' ')
    seq_n *= -3
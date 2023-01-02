# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
#  Напишите программу, определяющую, присутствует ли в заданном списке число, полученное от пользователя.


import os
clear = lambda: os.system('cls')
clear()

# import random
from random import sample

def find_number(amount, user_number):
    new_list = sample(range(1, amount+1), k=amount)
    print(new_list)
    if user_number in new_list:
        return 'yes'
    return 'no'

some_number = find_number(int(input('Enter amount - ')), 
                            int(input('Enter the desired number - ')))
print (some_number)
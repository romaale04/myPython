# Функции:

# with open('file.txt', 'a') as data:
#  data.write('line 11\n')
#  data.write('line 22\n')


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('\n LINE12 \n')
# data.write('LINE13 \n')
# data.close()

# exit()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data: 
#  print(line)
# data.close()
# exit()


# def new_string(symbol, count = 3):
#     return(symbol * count)
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(4))




            # Рекурсия:


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#          return fib(n - 1) + fib (n -2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)




            # Кортежи - неизменяемый список:
            
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


#             Множества:

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set(

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# #  {1, 21, 3, 13}


            # Списки:
# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


# list1[0] = 123
# list2[1] = 234


# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


list1 = [1,2,3,4,5]
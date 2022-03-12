# city1 = len(input())
# city2 = len(input())
# city3 = len(input())
#
# a = min(city1, city2, city3)
# b = max(city1, city2, city3)
# c = (city1 + city2 + city3) - (a + b)
#
# if b - c == c - a:
#     print('YES')
# else:
#     print('NO')
#
# for i in range(6):
#     print('AAA')
# for j in range(5):
#     print('BBBB')
# print('E')
# for k in range(9):
#     print('TTTTT')
# print('G')

# n = int(input())
# for i in range(n+1):
#     print('квадрат числа', i, 'равен', i**2)


# n = int(input())
# for i in range(1, 11):
#     print(n,'x', i, '=',n*i)

# i = 123
# print(i % 10)


# counter1 = 0
# counter2 = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# counter1 = 0
# counter2 = 0
# for i in range(10):
#      a = int(input())
#      counter1 = counter1 + a
#      counter2 = counter2 + 1
# print(counter1 / counter2)


# n = int(input())
# counter = 0
# for i in range(n):
#     temp = int(input())
#     counter += temp
# print(counter)


# 1. Не забывайте про импорт модуля math, логарифм без него не будет работать.
#
# 2. Создайте переменную, у меня это num = 0.
#
# 3. range начинайте с цифры 1 до n , чтобы не начиналось с нуля.
#
# 4. num равно num + (1 / ( i  +  1), где первая единица - числитель, а ' i  + 1 ' знаменатель.  Тоесть сейчас мы решили дробные уравнения 1/2  +  1/3  +  1/4  ..... 1 / n. Первую единицу и логарифм мы не считали.
#
# 5. Вводим num2.
# num 2 = num + 1 ( та единица которую упустили) + логарифм.
# 6. print (num2)


# counter1 = 0
# sum = 0
# avg = 0
# for i in range(1, 11):
#     num = int(input('Введи число: '))
#     if num >= 10:
#         counter1 = counter1 + 1
#         sum = sum + num
#         avg = sum / counter1
# print(sum)
# print(counter1)
# print(avg)

# largest = -1
# smallest = 0
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print('наибольшее число', largest)
# print('наименьшее число', smallest)

# a = int(input())
# b = int(input())
# counter1 = 0
# for i in range(a, b+1):
#     if i % 10 == 4 or i % 10 == 9:
#         counter1 += 1
# print(counter1)

# n = int(input())
# total = 0
# for i in range(n):
#     num = int(input())
#     total += num
# print(num)

# n = int(input())
# sum = 0
#
# for i in range(1, n+1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         sum += i
# print(sum)

# n = int(input())
# total = 1
# for i in range(2, n+1):
#     total *= i
# print(total)


# num = int(input('Введи число: '))
# total = 0
#
#
# if num % 2 == 0:
#     total += 1
# else:
#     total -= 1
# print(total)

# largest = 0
# prelargest = 0
#
# n = int(input())
# for i in range(n):
#     num = int(input())
#     if num > largest:
#         largest = num
#         if largest > prelargest:
#             prelargest = num
#
# print(largest)
# print(largest)

# count1 = 0
# count2 = 0
#
# for i in range(10):
#     num = int(input())
#     count2 += 1
#     if num % 2 == 0:
#         count1 += 1
#     else:
#         count2 += 1
# if count1 == count2:
#     print('YES')
# else:
#     print('NO')

# fib1 = 0
# fib2 = 1
#
# n = int(input())
#
# print(fib2, end=' ')
#
# for i in range(0, n-1):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

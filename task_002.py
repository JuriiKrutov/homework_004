'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''
num = int(input('Введите число: '))
list = []
i = 2
while num != 1:
    if num % i == 0:
        num /= i
        list.append(i)
    else:
        i += 1
print(list)

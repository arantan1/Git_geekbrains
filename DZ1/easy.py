
__author__ = 'Иванов Сергей Сергеевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

a = int(input('Введите произвольное число: '))
while a>0:
    b=a%10
    a=a//10
    print(b)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('введите число a '))
b = int(input('введите число b '))
#1
#a,b = b,a
#print('a = ',a,'b = ',b)
#2
print('a = ',a+b-a,'b = ',a+b-b)
#3
#c = a + b
#a=c-a
#b=c-b
#print('a = ',a,'b = ',b)




# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите ваш возраст '))
if age>=18:
    print('Доступ разрешен')
else:
    print ('Извините, пользование данным ресурсом только с 18 лет')


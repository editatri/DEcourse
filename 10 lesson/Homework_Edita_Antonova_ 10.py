'''
1. Напишите код, который пытается преобразовать введённое пользователем значение в число.
Обработайте исключение ValueError, если пользователь введёт строку, не являющуюся числом.
'''

try:
    print(int(input('Введите значение: ')))
except ValueError:
    print('Введите число: ')


'''
2. Напишите программу, которая обрабатывает ввод целого числа пользователем. Если ввод
некорректен (например, буквы), программа должна вывести сообщение об ошибке.
'''

try:
    print(int(input('Enter number: ')))
except ValueError:
    print('Error')

'''
3. Напишите программу, которая просит пользователя ввести индекс элемента в списке и
выводит этот элемент. Обработайте исключение IndexError на случай ввода
недопустимого индекса.
'''

list = [10, 20, 44, 15]
ind = int(input('Enter element index: '))
try:
    print(list[ind])
except IndexError:
    print('Error')

'''
4. Напишите функцию, которая принимает список чисел и возвращает их среднее значение.
Обработайте исключение ZeroDivisionError, если список пустой.
'''

def listOfNumbers(list):
    sumOfNums = 0
    for arg in list:
        sumOfNums += int(arg)
    return sumOfNums/len(list)


a = [10, 20, 30]
try:
    print(listOfNumbers(a))
except ZeroDivisionError:
    print('Division by zero is prohibited.')
except ValueError:
    print('Check the entered value.')


'''
5. Напишите код, который использует try-except-else-finally, чтобы обработать
ошибку деления на ноль и вывести сообщение после завершения блока try.
'''

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
    print('Результат деления двух чисел: ', result)
except ZeroDivisionError:
    print("Делить на ноль нельзя.")
except ValueError:
    print("Проверьте введенное число.")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Программа завершена.")

'''
6. Напишите программу, которая запрашивает у пользователя два числа и выполняет деление.
Если ввод не является числом или деление на ноль, программа должна обрабатывать эти
исключения и продолжать запрашивать ввод до тех пор, пока не будут введены корректные
значения.
'''

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
    print('Результат деления двух чисел: ', result)
except ZeroDivisionError:
    print("Делить на ноль нельзя.")
    a = input("Введите первое число еще раз: ")
    b = input("Введите второе число еще раз: ")
    result = int(a)/int(b)
    print('Результат деления двух чисел: ', result)
except ValueError:
    print("Проверьте введенное число.")
    a = input("Введите первое число еще раз: ")
    b = input("Введите второе число еще раз: ")
    result = int(a)/int(b)
    print('Результат деления двух чисел: ', result)


'''
7. Напишите функцию, которая принимает список и индекс. Если индекс выходит за пределы
списка, функция должна выбрасывать пользовательское исключение и обрабатывать его в
основной программе.
'''

def func(list, index):
    print(list[index])

list = [10, 20, 30]
ind = 22

try:
    func(list, ind)
except IndexError:
    print('Check entered index.')

'''
8. Напишите программу, которая обрабатывает несколько возможных исключений:
ValueError, ZeroDivisionError и IndexError. Программа должна просить
пользователя ввести список чисел и индекс, по которому будет выполнено деление элемента
списка на введённое число.
'''

timesNumber = int(input('Введите количество элементов списка: '))
list = []
newList = []
def newFunc():
    for i in range(timesNumber):
        a = int(input(f'Введите {i+1} элемент списка: '))
        list.append(a)
    b = int(input('Введите индекс: '))
    for el in list:
        newList.append(int(el)/list[b])
    print(newList)

try:
    newFunc()
except ZeroDivisionError:
    print("Делить на ноль нельзя.")
except ValueError:
    print("Проверьте введенное число.")
except IndexError:
    print('Проверьте введенный индекс.')

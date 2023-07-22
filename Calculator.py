# Функция для сложения двух чисел
def add(x, y):
    return x + y

# Функция для вычитания двух чисел
def subtract(x, y):
    return x - y

# Функция для умножения двух чисел
def multiply(x, y):
    return x * y

# Функция для деления двух чисел
def divide(x, y):
    return x / y

print("Виберіть операцію.")
print("1. Додавання")
print("2. Віднімання")
print("3. Розмноження")
print("4. Поділ")

# Запросить у пользователя выбор операции.
choice = input("Введіть номер операції (1/2/3/4): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Неправильне введення.")

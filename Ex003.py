# Задание 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, 
# округлённую до трёх знаков после точки.
# Для n = 6 -> 14.072

n = int(input('Введите число: '))
a = []
b = 1
sum = 0
for i in range(1, n+1):
    b = (1+(1/i))**i
    a.append(round(b, 3))
    sum = sum + b
print(a)
print(round(sum, 3))
    

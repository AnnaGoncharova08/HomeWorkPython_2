# Задание 5. Реализуйте алгоритм перемешивания списка.

import random
n = [1, 2, 'hello', 5, 8.47, 'bye']
a = random.sample(n, len(n))
print(a)
# Напишите функцию, возвращающую наибольшее из двух чисел
def my_max(n1, n2):
    if n1<n2:
        return n2
    else:
        return n1
print(my_max(5, 6))
print(my_max(-10, -12))
print(my_max(2.5, 2.6))
print(my_max(-2.5, 0))
print(my_max(0, -2.5))
print(my_max(5, 5))

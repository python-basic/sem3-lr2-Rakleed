from math import sqrt

def main ():
    print("Программа ищет площадь треугольника, используя формулу Герона.\n")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    result = geron_sq(a, b, c)

    print("\nПлощадь треугольника = " + str(result))

def geron_sq(a, b, c):
    p = 1 / 2 * (a + b + c) # Вычисление полупериметра
    return sqrt(p * (p - a) * (p - b) * (p - c)) # Вычисление площади треугольника

main()

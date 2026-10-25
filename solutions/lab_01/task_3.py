import math
#Часть 1
x = 17
y = 5
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)
#Часть 2
print(2 ** 1000)
#Часть 3
result = 0.1 + 0.2
print(result)
print(result == 3)
print(result - 0.3)
print(math.isclose(result, 0.3))
#Часть 4
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(1), type(bool(1)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))
z = complex(2, -3)
print(z, type(z))
print("действительная часть:", z.real)
print("мнимая часть:", z.imag)
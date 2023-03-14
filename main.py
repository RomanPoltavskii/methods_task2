# 2sin(ln x^4)+cth x= 0, (2<=x<=15)
import math


def f(x):
    return math.sin(math.log(x**4)) * 2 + (math.cosh(x) / math.sinh(x))


def chord(f, a, b, eps=1e-5):
    x = (f(b)*a-f(a)*b) / (f(b) - f(a))
    while abs(b - a) >= eps:
        x = (f(b)*a-f(a)*b) / (f(b) - f(a))
        #x = a - (f(a)*((b-a) / (f(b) - f(a))))
        if (f(x) * f(a)) <= 0:
            b = x
        else:
            a = x
    return x


x1 = chord(f, 2, 3.6)
x2 = chord(f, 3, 6)
x3 = (chord(f, 11.5, 15))

print('Первый корень ' + str(x1))
print(str(f(x1)) + '\n')
print('Второй корень ' + str(x2))
print(str(f(x2)) + '\n')
print('Третий корень ' + str(x3))
print(str(f(x3)) + '\n')

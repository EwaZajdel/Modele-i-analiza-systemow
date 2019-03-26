#0 Use alternative way of reading inputs - using library (0.5p)
#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
import math
from cs50 import get_int, get_float

print("-"*80)
print("zadanie 1")
def obwod(r):
    return 2*math.pi*r

def pole(r):
    return math.pi*r**2

print("podaj promien dla pierwszego kola: ")
x = get_int()
while x < 0:
    print("liczba nie moze byc ujemna. podaj promien dla pierwszego kola: ")
    x = get_int()

print("podaj promien dla drugiego kola: ")
y = get_int()
while y < 0:
    print("liczba nie moze byc ujemna. podaj promien dla drugiego kola: ")
    y = get_int()

print("kolo 1 ")
print("obwod: ", obwod(x))
print("pole: ", pole(x))
print("kolo 2 ")
print("obwod: ", obwod(y))
print("pole: ", pole(y))


#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
print("-"*80)
print("zadanie 2")

print("podaj x: ")
x = get_float()

print("podaj y: ")
y = get_float()
while y == 0:
    print("Nie dziel przez 0, podaj y: ")
    y = get_float()


prawda = 1
nieparzysta = 0
while prawda:
    while (x % y) != 0:
        print(x, " Nie jest podzielne przez ", y, "\npodaj x: ")
        x = get_float()
        print("podaj y: ")
        y = get_float()
    if x % 2 != 0:
        print(x, " nie jest liczba parzysta")
        nieparzysta = 1
    if y % 2 != 0:
        print(y, "nie jest liczba parzysta")
        nieparzysta = 1
    if nieparzysta == 0:
        prawda = 0
    if nieparzysta == 1:
        print("podaj x: ")
        x = get_float()
        print("podaj y: ")
        y = get_float()
        nieparzysta = 0

print(x, "jest podzielne przez", y, "\nobie liczby sa parzyste")


#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
print("-"*80)
print("zadanie 3")
print("podaj x: ")
x = get_float()
print("podaj y: ")
y = get_float()
while y == 0:
    print("Nie dziel przez 0, podaj y: ")
    y = get_float()


print("x jest podzielne przez y") if x % y == 0 else print("x nie jest podzielne przez y")


#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number
# of decimals". (1p)
print("-"*80)
print("zadanie 4")
print(x, "/", y, "=")
print("%.2f" % (x/y))

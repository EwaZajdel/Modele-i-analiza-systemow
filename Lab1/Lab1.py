from numpy import *
from matplotlib.pyplot import *
import math
print ("1.1")
for x in range(56, 101):
    y = 2*x**2+2*x+2
    print(y)


print('-'*20)

print("1.2")
print('Insert your value here:')
x = int(input())
print('The factorial value', math.factorial(x))

print('-'*20)


print("1.3")

def minimum(a):

    minpos = a.index(min(a))
    mindigit = min(a)

    print("The maximum is at position", minpos + 1)
    print("Minimum digit", mindigit)

a = [3, 4, 1, -5, 4, 5, 10, -10]
minimum(a)

print('-'*20)

print("1.4")

print("How many points should the chart have")
chart = int(input())
show()

x = linspace(-20, 20, chart)
y = (x-4)*(x+4)

plot(x, y)
show()

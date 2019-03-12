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


print("Insert 5 numbers to an array:")
tab = [0, 0, 0, 0, 0]
for i in range(0, 5):
    tab[i] = int(input())

print("Inserted array: ", tab)

def lowest(tab):
    min = tab[0]
    amount = 0
    for i in range(0, len(tab)):
        if (tab[i] < min):
            min = tab[i]
    print("The lowest value is: ", min)
    print("It is in position: ")
    for i in range(0, len(tab)):
        if (tab[i] == min):
            amount += 1
            print(i+1)


lowest(tab) 


print('-'*20)

print("1.4")

print("How many points should the chart have")
chart = int(input())
show()

x = linspace(-20, 20, chart)
y = (x-4)*(x+4)

plot(x, y)
show()

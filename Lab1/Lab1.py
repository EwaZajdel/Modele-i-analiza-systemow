from numpy import *
from matplotlib.pyplot import *
import math

print ("1.1")

for x in range(-20, 1):
   y = 2*x**2+2*x+2
   print(y)


print('-'*20)


print("1.2")




def user(x):
    print('Insert your value here:')

    x = float(input())
    try:
        print('The factorial value', math.factorial(x))

    except ValueError:
        print("You must choose positive number")


user(x)


print('-'*20)

print("1.3")




print("Podaj rozmiar tab:")
tab = []
s=int(input())
tabind=[]
print("Insert 6 numbers to an array:")
for i in range(0, s):

    tab.append(int(input()))


print("Inserted array: ", tab)


def lowest(tab):

    min = tab[0]


    for i in range(0, len(tab)):
        if (tab[i] < min):
            min = tab[i]

    print("The lowest value is: ", min)
    print("It is in position: ")


    for i in range(0, len(tab)):
        if (tab[i] == min):
            tabind.append(i)

    print(tabind)


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

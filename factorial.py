#факториал
from math import factorial


num = int (input ("введите число "))
factorial = 1
for i in range (1, num+1):
    factorial *= i
    print (factorial, end =" " )
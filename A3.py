#Ques3

import math

a=int(input("Enter length of first side= "))
b=int(input("Enter length of second side= "))
c=int(input("Enter length of third side= "))

if (a+b)>c and (a+c)>b and (b+c)>a:
    s= (a+b+c)/2
    area_square=s*(s-a)*(s-b)*(s-c)
    area= math.sqrt(area_square)
    print("Area of the Triangle using Heron's Formula= ",area,"sq. units")
else:
    print("Triangle invalid")
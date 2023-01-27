#Ques1

string=str(input("Enter a string: "))
x=""

for i in range(len(string)):
    x=string[i]+x
print(x)
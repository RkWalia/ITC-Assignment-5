#Ques6

start_point=int(input("Enter the starting point of range= "))
end_point=int(input("Enter the ending point of range= "))

for i in range(start_point,end_point+1):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i)
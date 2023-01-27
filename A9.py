#Ques9

string = ' '.join(input("Enter a srting: ").split())
list1 = string.split()
for i in set(list1):
    print(i, 'occurs:',list1.count(i), 'times')
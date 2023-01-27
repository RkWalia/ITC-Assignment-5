#Ques5

Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alphabet1 = list(map(str,Alphabet))

row = int(input("Enter the number of rows:"))
x = 0
y = 1
letters = ((row)*(row + 1))//2
if letters > 26:
    Alphabet *= (letters//26) + 1
    Alphabet1 = list(map(str,Alphabet))
for i in range(row):
    y = x + i+ 1
    print(Alphabet[x:y])
    x += i + 1
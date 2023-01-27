#Ques8

inp = list(map(int, input('Enter 10 numbers with \' \' separator: ').split()))

posi = []
negi = []
odd = []
even = []

for i in inp:
    if i > 0: posi.append(i)
    if i<0: negi.append(i)
    if i%2 == 0: even.append(i)
    else: odd.append(i)
print('Positive Numbers: ', posi)
print('Negative Numbers: ', negi)
print('Odd Numbers: ', odd)
print('Even Numbers: ', even)
for i in set(inp):
    print(i, 'occurs :', inp.count(i), 'times')
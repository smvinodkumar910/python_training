
rows = 10

for i in range(rows):
    for j in range(i+1,0,-1):
        print(i+1,end='')
    print('')
'''
1
22
333
4444
55555
'''


for i in range(rows):
    for j in range(1,i+2,1):
        print(j,end='')
    print('')

'''
1
12
123
1234
12345
'''
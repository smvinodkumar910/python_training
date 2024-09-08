
rows = 5

for i in range(rows):
    for j in range(i+1,0,-1):
        print('*',end='')
    print('')


for i in range(1,rows):
    for j in range(rows-i,0,-1):
        print('*',end='')
    print('')
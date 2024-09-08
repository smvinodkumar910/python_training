
rows = 5
spaces = 10

for i in range(rows):
    for j in range(spaces,0,-1):
        print(end=' ')
    spaces = spaces-1
    for j in range(i+1,0,-1):
        print('*',end = ' ')
    print('')
spaces = spaces+1
for i in range(1,rows):
    spaces = spaces+1
    for j in range(spaces,0,-1):
        print(end=' ')
    for j in range(rows-i,0,-1):
        print('*',end = ' ')
    print('')
    
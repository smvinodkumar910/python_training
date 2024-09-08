
rows = 10
spaces = 20


for i in range(rows):
    for j in range(spaces):
        print(end=' ')
    spaces=spaces+1
    for j in range(rows-i,0,-1):
        print('*',end=' ')
    print('')

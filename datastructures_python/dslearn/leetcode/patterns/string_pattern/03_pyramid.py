
rows = 6
spaces = 20


for i in range(rows):
    for j in range(spaces,0,-1):
        print(end=' ')
    spaces=spaces-1
    for j in range(i+1,0,-1):
        print('*',end=' ')
    print('')

lis = []
for i in range(int(input())):
    inp = input().split()
    if inp[0] == 'remove':
        if int(inp[1]) in lis:
            lis.remove(int(inp[1]))
    elif inp[0] == 'insert':
        lis.insert(int(inp[1]),int(inp[2]))
    elif inp[0] == 'append':
        lis.append(int(inp[1]))
    elif inp[0] == 'sort':
        lis.sort()
    elif inp[0] == 'print':
        print(lis)
    elif inp[0] == 'reverse':
        lis.reverse()
    elif inp[0] == 'pop':
        lis.pop()

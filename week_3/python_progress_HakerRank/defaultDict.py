from collections import defaultdict

n , m = [int(i) for i in input().split()]

a  = defaultdict(list)
for i in range(n):
    char = input()
    a[char].append(str(i+1))
for i in range(m):
    char = input()
    if char in a:
        print(" ".join( a[char]))
    else:
        print(-1)

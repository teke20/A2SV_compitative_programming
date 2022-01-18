from collections import deque
d = deque()
n = int(input())
for i in range(n):
    opo = input().split()
    if opo[0] == "append":
        d.append(opo[1])
    elif opo[0] == "pop":
        d.pop()
    elif opo[0] == "popleft":
        d.popleft()
    elif opo[0] == "appendleft":
        d.appendleft(opo[1])

print(' '.join(d))


from collections import Counter 
x = input()
S = Counter(map(int, input().split()))
cus = input()
N = int(cus)
earning = 0 
for i in range(N):
    size, price = map(int, input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earning += price
print(earning)

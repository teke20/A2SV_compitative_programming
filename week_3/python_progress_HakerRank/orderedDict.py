# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

od=dict()
for i in range(int(input())):
    k,v=input().rsplit(' ',1)
    if k in od:
        od[k]=int(od[k])+int(v)
    else:
        od[k]=v    
for k,v in od.items():
    print(k,v)

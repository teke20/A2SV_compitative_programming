from itertools import product
def cartesian_product(arr1, arr2):
    return list(product(arr1, arr2))

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*cartesian_product(a,b))

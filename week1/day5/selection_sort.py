class Solution: 
    def selectionSort(self, arr, n):
        # code here 
        m = len(arr)
        for i in range(0,m-1):
            first = i
            
            for j in range(i+1,m):
                if arr[j]<arr[first]:
                    first = j
            
            if first != i:
                arr[first], arr[i] = arr[i], arr[first]
        return arr
#  driver code goes here

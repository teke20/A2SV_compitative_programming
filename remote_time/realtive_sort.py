class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        out = []
        for value2 in arr2:
            for index,value1 in enumerate(arr1):
                if value2 == value1:
                    out.append(arr1[index])
                    arr1[index] = None
        remainder_arr1 = list(filter(None,arr1))
        out = out+sorted(remainder_arr1)
        return out

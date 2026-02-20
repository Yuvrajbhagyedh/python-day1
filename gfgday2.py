from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        
        # Step 1: Convert integers to strings
        arr = list(map(str, arr))
        
        # Step 2: Define custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            else:
                return 0
        
        # Step 3: Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Step 4: Edge case (all zeros)
        if arr[0] == "0":
            return "0"
        
        # Step 5: Join and return
        return ''.join(arr)
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
      
        for num in arr2:
            count = 0
            for x in arr1:
                if x == num:
                    count += 1
       
            for _ in range(count):
                result.append(num)
          
            arr1 = [x for x in arr1 if x != num]

      
        n = len(arr1)
        for i in range(n):
            for j in range(n-i-1):
                if arr1[j] > arr1[j+1]:
                    arr1[j], arr1[j+1] = arr1[j+1], arr1[j]

      
        result.extend(arr1)

        return result
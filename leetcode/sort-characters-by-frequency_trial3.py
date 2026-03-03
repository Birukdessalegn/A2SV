class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        arr = list(freq.items())
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j][1] < arr[j+1][1]:  
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        res = ""

        for char,count in arr:
            for i in range(count):
                res += char

        return res
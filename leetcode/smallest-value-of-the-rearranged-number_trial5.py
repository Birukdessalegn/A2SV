class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            a = list(map(int, str(num)))
            a.sort()
            if a[0] == 0:
                for i in range(1, len(a)):
                    if a[i] != 0:
                        a[0], a[i] = a[i], a[0]
                        break
            return int("".join(map(str, a)))
        else:
            a = list(map(int, str(-num)))
            a.sort(reverse=True)
            return -int("".join(map(str, a)))
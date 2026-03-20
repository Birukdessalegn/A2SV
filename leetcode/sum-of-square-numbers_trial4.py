class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))
        while a <= b:
            num = a*a + b*b
            if num == c:
                return True
            elif num < c:
                a += 1
            else:
                b -= 1
        return False

            
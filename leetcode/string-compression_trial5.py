class Solution:
    def compress(self, chars: List[str]) -> int:
        r = 0
        w = 0
        while r < len(chars):
            current_char = chars[r]
            count = 0
            while r < len(chars) and current_char == chars[r]:
                count += 1
                r += 1
            chars[w] = current_char
            w += 1
            if count > 1: 
                for c in str(count):
                    chars[w] = c
                    w += 1
        return w
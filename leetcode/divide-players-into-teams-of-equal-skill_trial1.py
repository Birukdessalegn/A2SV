class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        final = 0
        n = len(skill)
        i = 0
        j = n-1
        total = skill[i] + skill[j]
        while i < j:

            if skill[i]+skill[j] != total:
                return -1
            final += skill[i]*skill[j]
            i +=1
            j -=1
        return final

        
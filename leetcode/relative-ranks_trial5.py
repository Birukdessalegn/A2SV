from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}
        
        for i in range(n):
            s = sorted_scores[i]
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)
        
        answer = []
        for s in score:
            answer.append(rank_map[s])
        
        return answer
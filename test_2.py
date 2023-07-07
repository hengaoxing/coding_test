from typing import List

def compute_matches(teamA: List[int], teamB: List[int]) -> List[int]:
    teamA.sort()
    res = []
    for b in teamB:
        # When the number of matches is large,the algorithm can consider using the dichotomy
        count = 0
        for a in teamA:
            if a <= b:
                count += 1
        res.append(count)
    return res
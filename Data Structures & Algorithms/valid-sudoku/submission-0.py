class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rSet = defaultdict(set)
        cSet = defaultdict(set)
        sqSet = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                curr = board[r][c]
                sq = (r//3,c//3)
                if curr == '.':
                    continue
                if(
                    curr in rSet[r] or
                    curr in cSet[c] or
                    curr in sqSet[sq]
                ):
                    return False
                
                rSet[r].add(curr)
                cSet[c].add(curr)
                sqSet[sq].add(curr)
        
        return True
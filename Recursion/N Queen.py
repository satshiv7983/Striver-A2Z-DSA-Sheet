#User function Template for python3

class Solution:
    def nQueen(self, n):
        
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [[-1] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy=[0]*n
                for row in range(n):
                    for c in range(n):
                        if board[row][c]!=-1:
                            copy[row]=c+1
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = c

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = -1

        backtrack(0)
        return res
            

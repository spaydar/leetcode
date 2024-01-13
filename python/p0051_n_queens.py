from typing import List

def n_queens(n: int) -> List[List[str]]:
    result = []
    cols = set()
    pos_diags = set()
    neg_diags = set()
    curr: List[str] = []
    def place_queen(i: int) -> str:
        chars = []
        for x in range(n):
            chars.append('Q' if i == x else '.')
        return ''.join(chars)
    def dfs(row: int):
        if row == n:
            result.append(curr[:])
            return
        for col in range(n):
            pos_diag = row + col
            neg_diag = row - col
            if (col not in cols and
                pos_diag not in pos_diags and
                neg_diag not in neg_diags):
                cols.add(col)
                pos_diags.add(pos_diag)
                neg_diags.add(neg_diag)
                curr.append(place_queen(col))
                dfs(row + 1)
                curr.pop()
                cols.remove(col)
                pos_diags.remove(pos_diag)
                neg_diags.remove(neg_diag)
    dfs(0)
    return result

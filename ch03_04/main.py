import itertools


class BipartiteMatching(object):
    def __init__(self, sl: int, sr: int):
        self.size_left = sl
        self.size_right = sr
        self.lst: list[list[int]] = [[] for _ in range(sl)] 
        self.l2r: list[int] = []
        self.r2l: list[int] = []

    
    def add_edge(self, l: int, r: int):
        self.lst[l].append(r)


    def dfs(self, l: int, seen: list[bool]) -> bool:
        if seen[l]:
            return False
        seen[l] = True

        for r in self.lst[l]:
            if self.r2l[r] == -1 or self.dfs(self.r2l[r], seen): 
                self.l2r[l] = r
                self.r2l[r] = l
                return True
        return False

    
    def solve(self) -> list[tuple[int, int]]:
        res: list[tuple(int, int)] = [] 
        self.l2r = [-1] * self.size_left
        self.r2l = [-1] * self.size_right
        while True:
            update = False
            seen = [False] * self.size_left
            for l in range(self.size_left):
                if self.l2r[l] != -1:
                    continue
                if self.dfs(l, seen):
                    update = True
                    break
            if not update:
                break
        
        for l in range(self.size_left):
            if self.l2r[l] != -1:
                res.append((l, self.l2r[l]))
        return res


def solve(board: list[list[str]]) -> int:
    dx = [1, 0, -1,  0]
    dy = [0, 1,  0, -1]
    h = len(board)
    w = len(board[0])
    bm = BipartiteMatching(h*w, h*w)
    for i, j in itertools.product(range(h), range(w)):
        if board[i][j] == 'x':
            continue
        if (i+j)%2 == 1:
            continue
        for dir in range(4):
            ni = i + dx[dir]
            nj = j + dy[dir]
            if ni<0 or ni>=h or nj<0 or nj>=w:
                continue
            if board[ni][nj] == 'x':
                continue
            bm.add_edge(i*w+j, ni*w+nj)

    res = bm.solve()
    for l, r in res:
        li = l // w
        lj = l %  w
        ri = r // w
        rj = r %  w
        if li == ri:
            board[li][lj] = '-'
            board[ri][rj] = '-'
        else:
            board[li][lj] = '|'
            board[ri][rj] = '|'
    return len(res)


if __name__ == '__main__':
    print("Domino Tiling Input:")
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    max_num = solve(board)
    print(f'num of domino: {max_num}')
    for row in board:
        print(row)

Cell = int
Color = int
Stones = int

SIZE = 4
INF = SIZE*SIZE

BLACK: Color = 1
WHETE: Color = 0

def move(cell: Cell, dir: int) -> Cell:
    DX = [1, 0, -1,  0, 1,  1, -1, -1]
    DY = [0, 1,  0, -1, 1, -1, -1,  1]
    x = cell // SIZE + DX[dir]
    y = cell %  SIZE + DY[dir]
    if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
        return -1
    else:
        return x * SIZE + y


def iscolor(black: Stones, white: Stones, col: Color, cell: Cell) -> bool:
    if cell == -1:
        return False
    elif col == BLACK:
        return ((black >> cell) & 1) != 0
    else:
        return ((white >> cell) & 1) != 0


def put(black: Stones, white: Stones, col: Color, cell: Cell) -> Cell:
    if (((black | white) >> cell) & 1) != 0:
        return 0

    res = 0
    for dir in range(8):
        rev = 0
        cell2 = move(cell, dir)
        while iscolor(black, white, 1-col, cell2):
            rev |= 1 << cell2
            cell2 = move(cell2, dir)
        if iscolor(black, white, col, cell2):
            res |= rev
    
    return res


def calc(black: Stones, white: Stones, col: Color) -> int:
    num_black = 0
    num_white = 0
    num_empty = 0
    for cell in range(SIZE*SIZE):
        if ((black>>cell)&1) != 0:
            num_black += 1
        elif ((white>>cell)&1) != 0:
            num_white += 1
        else:
            num_empty += 1
    
    if num_black > num_white:
        num_black += num_empty
    elif num_black < num_white:
        num_white += num_empty

    if col == BLACK:
        return num_black - num_white
    else:
        return num_white - num_black


def rec(alpha: int, beta: int, black: Stones, white: Stones, col: Color) -> int:
    mine: list[Cell] = []
    opp: list[Cell] = []
    for cell in range(SIZE*SIZE):
        if put(black, white, col, cell) > 0:
            mine.append(cell)
        if put(black, white, 1-col, cell) > 0:
            opp.append(cell)
    
    if len(mine) == 0 and len(opp) == 0:
        return calc(black, white, col)

    if len(mine) == 0:
        return -rec(-beta, -alpha, black, white, 1-col)

    res = -INF
    for cell in mine:
        rev = put(black, white, col, cell)
        black2 = black ^ rev
        white2 = white ^ rev

        if col == BLACK:
            black2 |= 1 << cell
        else:
            white2 |= 1 << cell

        score = -rec(-beta, -alpha, black2, white2, 1-col)
        res = max(res, score)
        if res >= beta:
            return res
        alpha = max(alpha, res)
    
    return res


if __name__ == '__main__':
    black = (1<<6) | (1<<9)
    white = (1<<5) | (1<<10)
    print(rec(-INF, INF, black, white, BLACK))
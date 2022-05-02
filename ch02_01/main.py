import copy
import itertools

Field = list[list[int]]

class Sudoku(object):
    def __init__(self):
        self.field: Field = [[-1]*9 for _ in range(9)]
    
    def put(self, x: int, y: int, val: int):
        self.field[x][y] = val
    
    def reset(self, x: int, y: int):
        self.field[x][y] = -1
    
    def input(self):
        for x in range(9):
            line = input()
            for y in range(9):
                if line[y] == '*':
                    continue
                self.put(x, y, int(line[y]))
    
    def find_empty(self) -> tuple[int, int]:
        for x, y in itertools.product(range(9), repeat=2):
            if self.field[x][y] == -1:
                return (x, y)
        return (-1, -1)

    def find_choice(self, x: int, y: int) -> list[int]:
        cannot_use = set()
        for i in range(9):
            if self.field[x][i] != -1:
                cannot_use.add(self.field[x][i])
        
        for i in range(9):
            if self.field[i][y] != -1:
                cannot_use.add(self.field[i][y])

        x2 = x//3*3
        y2 = y//3*3
        for i, j in itertools.product(range(x2, x2+3), range(y2, y2+3)):
            if self.field[i][j] != -1:
                cannot_use.add(self.field[i][j])
        
        return [i for i in range(1, 10) if not i in cannot_use]


def dfs(board: Sudoku, res: list[Field], all: bool):
    if not all and len(res) == 0:
        return

    x, y = board.find_empty()
    if x == -1 and y == -1:
        res.append(copy.deepcopy(board.field))
        return
    
    can_use = board.find_choice(x, y)
    for val in can_use:
        board.put(x, y, val)
        dfs(board, res, all)
        board.reset(x, y)


def solve(board: Sudoku, all: bool) -> list[Field]:
    res: list[Field] = []
    dfs(board, res, all)
    return res
    

if __name__ == '__main__':
    print("Sudoku Input:")
    board = Sudoku()
    board.input()
    res = solve(board, True)

    if len(res) == 0:
        print("No Solutions.")
    elif len(res) > 1:
        print("More than one solution.")
    else:
        answer = res[0]
        for row in answer:
            print(''.join(map(str, row)))


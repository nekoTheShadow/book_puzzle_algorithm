import copy
import random
import solver

def write(board: solver.Sudoku):
    field = board.field
    for x in range(9):
        print(''.join("*" if field[x][y] == -1 else str(field[x][y]) for y in range(9)))


if __name__ == '__main__':
    board = solver.Sudoku()
    cells: list[tuple[int, int]] = []
    for x in range(9):
        line = input()
        for y in range(9):
            if line[y].isdigit():
                board.put(x, y, int(line[y]))
            elif line[y] == 'o':
                cells.append((x, y))

    res = solver.solve(board, False)
    for p in cells:
        board.put(p[0], p[1], res[0][p[0]][p[1]])
    
    res = solver.solve(board, True)
    score = len(res)
    print("initial problem : {0} sols".format(score))
    write(board)

    for it in range(10000):
        if score == 1:
            break
        
        board2 = copy.deepcopy(board)
        for con in range(2):
            x, y = random.choice(cells)
            board2.reset(x, y)
            can = board2.find_choice(x, y)
            val = random.choice(can)
            board2.put(x, y, val)

        res = solver.solve(board2, True)
        new_score = len(res)
        if new_score<score and new_score!=0:
            print(f"{it}:{score} sols -> {new_score} sols")
        board = board2
        score = new_score
        write(board)

print("final problem:")
write(board)    
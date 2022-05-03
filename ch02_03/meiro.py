import copy
import itertools


Cor = tuple[int, int]
DIR: list[Cor] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
NOTIN = -1

def solve(board: list[str], start: Cor, goal: Cor):
    h = len(board)
    w = len(board[0])

    nodes: list[list[Cor]] = []
    dist: list[list[int]] = [[NOTIN]*w for _ in range(h)]
    arrow: list[list[Cor]] = [[(NOTIN, NOTIN) for _ in range(w)] for _ in range(h)]
    
    nodes.append([start])
    dist[start[0]][start[1]] = 0

    while nodes:
        print(nodes)
        cur = nodes.pop()
        nxt: list[Cor] = []
        for x, y in cur:
            for direction in range(4):
                next_x = x + DIR[direction][0]
                next_y = y + DIR[direction][1]
                if next_x < 0 or next_x >= h: continue
                if next_y < 0 or next_y >= w: continue
                if board[next_x][next_y] == '#': continue
                if dist[next_x][next_y] != NOTIN: continue
                dist[next_x][next_y] = dist[x][y] + 1
                arrow[next_x][next_y] = (x, y)
                nxt.append((next_x, next_y))
        if nxt:
            nodes.append(nxt)

    if dist[goal[0]][goal[1]] == NOTIN:
        print("No Path")
        return

    res = list(map(list, board))
    cur_x, cur_y = goal
    while arrow[cur_x][cur_y] != (NOTIN, NOTIN):
        res[cur_x][cur_y] = 'o'
        cur_x, cur_y = arrow[cur_x][cur_y]

    print("-----solution-----")
    for s in res:
        print(''.join(s))
    print("length=", dist[goal[0]][goal[1]])


if __name__ == '__main__':
    print("Maze Input:")
    h, w = map(int, input().split())
    board = [input() for _ in range(h)]

    for x, y in itertools.product(range(h), range(w)):
        if board[x][y] == 'S': start = (x, y)
        if board[x][y] == 'G': goal = (x, y)

    solve(board, start, goal)
import itertools


Cor = tuple[int, int]

def get_digit(pos: Cor) -> int:
    return (pos[0]*4 + pos[1])*4


def get_val(pl: int, pos: Cor) -> int:
    pl >>= get_digit(pos)
    return pl & 0b1111


def read() -> tuple[int, Cor]:
    pl = 0
    for x in range(4):
        vals = list(map(int, input().split()))
        for y in range(4):
            if vals[y] == 0:
                emp = (x, y)
            else:
                pl += vals[y] << get_digit((x, y))
    return (pl, emp)


def write(pl: int):
    for x in range(4):
       print(' '.join(str(get_val(pl, (x, y))) for y in range(4))) 


def slide(pl: int, val: int, pos: Cor, emp: Cor) -> int:
    pl -= val << get_digit(pos)
    pl += val << get_digit(emp)
    return pl


def calc_distance(val: int, pos: Cor) -> int:
    x = (val-1) // 4
    y = (val-1) % 4
    return abs(x - pos[0]) + abs(y - pos[1])


def estimate_all(pl: int) -> int:
    res = 0
    for x, y in itertools.product(range(4), repeat=2):
        val = get_val(pl, (x, y))
        if val == 0:
            continue
        res += calc_distance(val, (x, y))
    return res


def estimate(est: int, val: int, pos: Cor, emp: Cor) -> int:
    return est + calc_distance(val, emp) - calc_distance(val, pos)


def dfs(max_depth: int, depth: int, pl: int, emp: Cor, est: int, pre_dir: int, res: list[int]):
    DX = [1, 0, -1,  0]
    DY = [0, 1,  0, -1]
    if len(res) > 0:
        return
    if est == 0:
        res.append(pl)
        return
    if depth >= max_depth:
        return
    
    for dir in range(4):
        reverse_dir = (dir + 2) % 4
        if reverse_dir == pre_dir:
            continue
        
        nx = emp[0] + DX[dir]
        ny = emp[1] + DY[dir]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        
        pos = (nx, ny)
        val = get_val(pl, pos)
        next_pl = slide(pl, val, pos, emp)
        next_est = estimate(est, val, pos, emp)

        if depth + next_est <= max_depth:
            dfs(max_depth, depth+1, next_pl, pos, next_est, dir, res)
            if len(res) > 0:
                res.append(pl)
                return


def solve(pl: int, emp: Cor) -> list[int]:
    est = estimate_all(pl)
    for max_depth in range(81):
        res = []
        dfs(max_depth, 0, pl, emp, est, -1, res)
        if len(res) > 0:
            res.reverse()
            return res
    return []




if __name__ == '__main__':
    print("15 puzzle input:")
    pl, emp = read()
    res = solve(pl, emp)
    for i in range(len(res)):
        print("-----")
        print(f"{i}th move:")
        write(res[i])
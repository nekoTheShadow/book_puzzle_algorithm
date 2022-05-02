import copy


class Fukumenzan(object):
    NOTIN = -1

    def __init__(self, problem: list[str]):
        self.problem: list[str] = problem
        self.board: list[list[int]] = [[-1]*len(problem[i]) for i in range(len(problem))]
        self.used: set[int] = set()


    def get_size(self) -> int: 
        return len(self.problem)


    def get_digit(self, row: int = -1) -> int: 
        return len(self.problem[row])
    

    def is_used(self, val: int) -> bool:
        return val in self.used

    
    def get_val(self, row: int, digit: int) -> int:
        if digit >= self.get_digit(row):
            return 0
        else:
            return self.board[row][self.get_digit(row)-1-digit]
    

    def get_char(self, row: int, digit: int) -> str:
        return self.problem[row][self.get_digit(row)-1-digit]

    
    def print(self):
        for vec in self.board:
            print(''.join(map(str, vec)))
    

    def set_val(self, row: int, digit: int, val: int):
        c = self.get_char(row, digit)
        for r in range(self.get_size()):
            for d in range(self.get_digit(r)):
                if self.problem[r][d] == c:
                    self.board[r][d] = val
        self.used.add(val)

    
    def reset_val(self, row: int, digit: int, val: int):
        c = self.get_char(row, digit)
        for r in range(self.get_size()):
            for d in range(self.get_digit(r)):
                if self.problem[r][d] == c:
                    self.board[r][d] = -1
        self.used.remove(val)


    def is_valid(self) -> bool:
        for val in self.board:
            if val[0] == 0:
                return False
        
        kuriagari = 0
        for digit in range(self.get_digit()):
            tot = 0
            for row in range(self.get_size()):
                if self.get_val(row, digit) == Fukumenzan.NOTIN:
                    return True
                if row != self.get_size() - 1:
                    tot += self.get_val(row, digit)
            tot += kuriagari
            kuriagari = tot // 10
            if tot % 10 != self.get_val(self.get_size() - 1, digit):
                return False
        
        return kuriagari == 0


def dfs(fu: Fukumenzan, row: int, digit: int, res: list[Fukumenzan]):
    if row == 0 and digit == fu.get_digit():
        res.append(copy.deepcopy(fu))
        return

    next_row = row + 1
    next_digit = digit
    if next_row == fu.get_size():
        next_row = 0
        next_digit = digit + 1

    if fu.get_val(row, digit) != -1:
        dfs(fu, next_row, next_digit, res)
    else:
        for val in range(10):
            if fu.is_used(val):
                continue
            fu.set_val(row, digit, val)
            if fu.is_valid():
                dfs(fu, next_row, next_digit, res)
            fu.reset_val(row, digit, val)


def solve(fu: Fukumenzan) -> list[Fukumenzan]:
    for i in range(fu.get_size()-1):
        if fu.get_digit(i) > fu.get_digit():
            return []
    res = []
    dfs(fu, 0, 0, res)
    return res


if __name__ == '__main__':
    print("Fukumenzan Input:")
    
    n = int(input())
    problem = [input() for _ in range(n)]
    fu = Fukumenzan(problem)
    res = solve(fu)

    print("The num of solutions:")
    for i in range(len(res)):
        print(f"{i+1} th solution:")
        res[i].print()

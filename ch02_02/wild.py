import collections
import copy

class WildFukumenzan(object):
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
        if c == "?":
            self.board[row][self.get_digit(row)-1-digit] = val
            return 
        
        for r in range(self.get_size()):
            for d in range(self.get_digit(r)):
                if self.problem[r][d] == c:
                    self.board[r][d] = val
        self.used.add(val)

    
    def reset_val(self, row: int, digit: int, val: int):
        c = self.get_char(row, digit)
        if c == "?":
            self.board[row][self.get_digit(row)-1-digit] = WildFukumenzan.NOTIN
            return 
        
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
                if self.get_val(row, digit) == WildFukumenzan.NOTIN:
                    return True
                if row != self.get_size() - 1:
                    tot += self.get_val(row, digit)
            tot += kuriagari
            kuriagari = tot // 10
            if tot % 10 != self.get_val(self.get_size() - 1, digit):
                return False
        
        return kuriagari == 0


def dfs(fu: WildFukumenzan, row: int, digit: int, res: list[WildFukumenzan]):
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
            if fu.get_char(row, digit) != '?' and fu.is_used(val):
                continue
            fu.set_val(row, digit, val)
            if fu.is_valid():
                dfs(fu, next_row, next_digit, res)
            fu.reset_val(row, digit, val)


def solve(fu: WildFukumenzan) -> list[WildFukumenzan]:
    for i in range(fu.get_size()-1):
        if fu.get_digit(i) > fu.get_digit():
            return []
    res = []
    dfs(fu, 0, 0, res)
    return res


def makeup(inpt: list[str], sols: list[WildFukumenzan]) -> list[list[str]]:
    groups: collections.defaultdict[tuple, int] = collections.defaultdict(int)
    for sol in sols:
        dct: dict[int, str] = {}
        for row in range(len(inpt)):
            for i in range(len(inpt[row])):
                v = sol.get_val(row, len(inpt[row])-1-i)
                c = sol.get_char(row, len(inpt[row])-1-i)
                if c != '?':
                    dct[v] = c
        
        problem: list[str] = ["" for _ in inpt]
        new_moji = "a"
        for row in range(len(inpt)):
            for i in range(len(inpt[row])):
                v = sol.get_val(row, len(inpt[row])-1-i)
                c = sol.get_char(row, len(inpt[row])-1-i)
                if c != '?':
                    problem[row] += c
                elif v in dct:
                    problem[row] += dct[v]
                else:
                    dct[v] = chr(ord(new_moji)+1)
                    problem[row] += dct[v] 
        groups[tuple(problem)] += 1
    
    res: list[str] = []
    for group in groups:
        if groups[group] == 1:
            res.append(group)
    return res


if __name__ == '__main__':
    print("Fukumenzan Input:")
    n = int(input())
    inpt = [input() for _ in range(n)]

    fu = WildFukumenzan(inpt)
    sols = solve(fu)

    res = makeup(inpt, sols)
    for ans in res:
        print(ans)
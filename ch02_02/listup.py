import copy
import solver

dct: dict[str, int] = {}

def rec_makeup(words: list[str], num: int, problem: list[str], res: list[list[str]]):
    if len(problem) == num:
        tot = 0
        for i in range(len(problem)-1):
            tot += dct[problem[i]]
        if tot != dct[problem[-1]]:
            return
        fu = solver.Fukumenzan(problem)
        sols = solver.solve(fu)
        if len(sols) == 1:
            res.append(copy.deepcopy(problem))
        return

    for wd in words:
        problem.append(wd)
        rec_makeup(words, num, problem, res)
        problem.pop()

    
def makeup(words: list[str], num: int) -> list[list[str]]:
    res: list[list[str]] = []
    problem: list[str] = []
    rec_makeup(words, num, problem, res)
    return res


if __name__ == '__main__':
    num_words, num_rows = map(int, input().split())
    words: list[str] = []
    for i in range(num_words):
        wd, val = input().split()
        words.append(wd)
        dct[wd] = int(val)
    res = makeup(words, num_rows)
    for ans in res:
        print(ans)
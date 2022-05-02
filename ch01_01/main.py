import itertools

def calc_poland(exp: str) -> float:
    space: list[float] = []
    for c in exp:
        if c.isdigit():
            space.append(float(c))
        else:
            second = space.pop()
            first = space.pop()
            if c == '+': space.append(first+second)
            if c == '-': space.append(first-second)
            if c == '*': space.append(first*second)
            if c == '/': 
                if second == 0:
                    space.append(float('nan'))
                else:
                    space.append(first/second)
    return space.pop()

def decode_poland(exp: str) -> str:
    space: list[str] = []
    for c in exp:
        if c.isdigit():
            space.append(c)
        else:
            second = space.pop()
            first = space.pop()
            if c == '*' or c == '/':
                if len(first) > 1: first = f'({first})'
                if len(second) > 1: second = f'({second})'
            space.append(f'{first}{c}{second}')
    return space.pop()

def solve(val: list[int], target: int) -> list[str]:
    res: list[str] = []
    def check(exp: str):
        if abs(calc_poland(exp) - target) < 1e-9:
            res.append(decode_poland(exp))

    for v1, v2, v3, v4 in itertools.permutations(val):
        for op1, op2, op3 in itertools.product('+-*/', repeat=3):
            check(f'{v1}{v2}{v3}{v4}{op1}{op2}{op3}') # xxxxooo
            check(f'{v1}{v2}{op1}{v4}{v3}{op2}{op3}') # xxxoxoo
            check(f'{v1}{v2}{v3}{op1}{op2}{v4}{op3}') # xxxooxo
            check(f'{v1}{v2}{op1}{v3}{op2}{v4}{op3}') # xxoxoxo
            check(f'{v1}{v2}{op1}{v3}{v4}{op2}{op3}') # xxoxxoo
    return res

if __name__ == '__main__':
    val: list[int] = []
    for i in range(4):
        print(f'{i+1} th number: ', end='')
        val.append(int(input()))
    
    print('target number: ',  end='')
    target = int(input())

    res = solve(val, target)
    for exp in res:
        print(f'{exp}={target}')


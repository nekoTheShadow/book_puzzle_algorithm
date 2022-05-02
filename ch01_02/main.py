EMPTY = 0
PLUS = 1
MINUS = 2
MUL = 3
DIV = 4
TARGET = 100

def calc_empty(signs: list[int]) -> tuple[list[float], list[int]]:
    new_vals: list[float] = []
    new_signs: list[int] = []

    val = 1
    for i in range(len(signs)):
        add = i + 2
        if signs[i] == EMPTY:
            val = val * 10 + add
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = add

    new_vals.append(val)
    return (new_vals, new_signs)


def calc_mul_div(vals: list[float], signs: list[int]) -> tuple[list[float], list[int]]:
    new_vals: list[float] = []
    new_signs: list[int] = []

    val = vals[0]
    for i in range(len(signs)):
        add = vals[i+1]
        if signs[i] == MUL:
            val *= add
        elif signs[i] == DIV:
            val /= add
        else:
            new_vals.append(val)
            new_signs.append(signs[i])
            val = add

    new_vals.append(val)
    return (new_vals, new_signs)


def calc_plus_minus(vals: list[float], signs: list[int]) -> float:
    res = vals[0]
    for i in range(len(signs)):
        add = vals[i+1]
        if signs[i] == PLUS:
            res += add
        else:
            res -= add
    return res
    


def calc(signs: list[int]) -> float:
    step1 = calc_empty(signs)
    step2 = calc_mul_div(step1[0], step1[1])
    return calc_plus_minus(step2[0], step2[1])


def decode(sign: list[int]) -> str:
    res = "1"
    for i in range(len(sign)):
        if sign[i] == PLUS:
            res += "+"
        elif sign[i] == MINUS:
            res += "-"
        elif sign[i] == MUL:
            res += "*"
        elif sign[i] == DIV:
            res += "/"
        res += str(i+2)
    return res

def rec(vec: list[int], res: list[str]):
    if len(vec) == 8:
        if abs(calc(vec)-TARGET) < 1e-9:
            res.append(decode(vec))
        return

    for add in range(5):
        vec2 = list(vec)
        vec2.append(add)
        rec(vec2, res)

if __name__ == '__main__':
    vec: list[int] = []
    res: list[str] = []
    rec(vec, res)
    print(f"The number of solutions: {len(res)}")
    for ans in res:
        print(f"{ans}={TARGET}")
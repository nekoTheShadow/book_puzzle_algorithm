def is_valid(val: int, s: str) -> bool:
    t = str(val)
    if len(t) != len(s):
        return False
    for i in range(len(t)):
        if s[i] == '*':
            continue
        if t[i] != s[i]:
            return False
    return True


def is_valid_sub(v: int, k: int, s: str) -> bool:
    c = s[len(s)-1-k]
    if c == '*':
        return True
    return v == int(c)


def decode(vec: list[int]) -> int:
    res = 0
    order = 1
    for v in vec:
        res += order * v
        order *= 10
    return res


class Mushikuizan(object):
    def __init__(self, multiplicand: str, multiplier: str, product: str, middle: list[str]):
        self.multiplicand = multiplicand
        self.multiplier = multiplier
        self.product = product
        self.middle = middle
        self.res: list[tuple[int, int]] = []
    

    def rec_plier(self, plicand: int, vec: list[int]):
        if len(vec) == len(self.multiplier):
            plier = decode(vec)
            if not is_valid(plicand*plier, self.product):
                return
            self.res.append((plicand, plier))
            return
    
        for add in range(1, 10):
            if not is_valid_sub(add, len(vec), self.multiplier):
                continue
            if not is_valid(plicand*add, self.middle[len(vec)]):
                continue
            vec.append(add)
            self.rec_plier(plicand, vec)
            vec.pop()


    def rec_plicand(self, vec: list[int]):
        if len(vec) == len(self.multiplicand):
            vec2 = []
            self.rec_plier(decode(vec), vec2)
            return

        for add in range(10):
            if len(vec) == 0 and add == 0:
                continue
            if not is_valid_sub(add, len(vec), self.multiplicand):
                continue
            vec.append(add)
            self.rec_plicand(vec)
            vec.pop()

    
    def solve(self) -> list[tuple[int, int]]:
        self.res.clear()
        vec: list[int] = []
        self.rec_plicand(vec)
        return self.res


if __name__ == '__main__':
    print("Mushikuizan Input:")
    a, b = map(int, input().split())
    hijou = input()
    jou = input()
    middle = [input() for _ in range(b)]
    seki = input()

    mu = Mushikuizan(hijou, jou, seki, middle)
    res = mu.solve()

    print(f"The num of solutions: {len(res)}")
    for i, (first, second) in enumerate(res):
        print(f"{i} th solution: {first}*{second}={first*second}")




import collections
import copy


Node = tuple[int]

def solve(cap: Node, start: Node, goal: Node):
    dist = {start : 0}
    arrow: dict[Node, Node] = {}
    todo = collections.deque([start])

    while todo:
        cur = todo.popleft()
        for frm in range(3):
            for to in range(3):
                if frm == to: 
                    continue

                lst = list(cur)
                if lst[to]+lst[frm] <= cap[to]:
                    lst[to] += lst[frm]
                    lst[frm] = 0
                else:
                    lst[frm] = lst[frm]+lst[to]-cap[to]
                    lst[to] = cap[to]
                
                nxt = tuple(lst)
                if nxt in dist:
                    continue
                dist[nxt] = dist[cur] + 1
                arrow[nxt] = cur
                todo.append(nxt)

    if not goal in dist:
        print("Impossible")
        return

    res = []
    cur = goal
    while cur in arrow:
        res.append(cur)
        cur = arrow[cur]
    res.append(cur)

    res.reverse()
    for i in range(len(res)):
        print('{0} th: {1}'.format(i, ' '.join(map(str, res[i]))))


if __name__ == '__main__':
    print("Cap: ", end='')
    cap = tuple(map(int, input().split()))
    print("Start: ", end='')
    start = tuple(map(int, input().split()))
    print("Goal: ", end='')
    goal = tuple(map(int, input().split()))
    solve(cap, start, goal)


def solve(s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    dp = [[n+m]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for x in range(m+1):
        for y in range(n+1):
            if x > 0:
                dp[x][y] = min(dp[x][y], dp[x-1][y]+1)
            if y > 0:
                dp[x][y] = min(dp[x][y], dp[x][y-1]+1)
            if x > 0 and y > 0:
                length = 1
                if s[x-1] == t[y-1]:
                    length = 0
                dp[x][y] = min(dp[x][y], dp[x-1][y-1]+length)
    return dp[m][n]


if __name__ == '__main__':
    print("First String:")
    s = input()
    print("Second String:")
    t = input()
    print(solve(s, t))
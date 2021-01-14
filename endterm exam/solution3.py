import sys

MAX = 100
grid = []

for i in range(1000):
    temp1 = []
    for j in range(MAX):
        temp2 = []

        for k in range(MAX):
            temp2.append(0)
        temp1.append(temp2)

    grid.append(temp1)

def calc2(x, y):
    sumx = 0
    while x:
        sumx += x % 10
        x = x // 10

    sumy = 0

    while y:
        sumy += y % 10
        y = y // 10

    return sumx * sumy

def calc(arr, i, len, prev, n, k):

    if len == k:
        return 0

    if i == n:
        return -sys.maxsize - 1

    if grid[i][len][prev]:
        return grid[i][len][prev]

    if len & 1:
        inc = (calc2(arr[prev], arr[i]) + calc(arr, i + 1, len + 1, i, n, k))
    else:
        inc = calc(arr, i + 1, len + 1, i, n, k)

    exc = calc(arr, i + 1, len, prev, n, k)
    grid[i][len][prev] = max(inc, exc)
    return grid[i][len][prev]

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
print(calc(arr, 0, 0, 0, n, x))

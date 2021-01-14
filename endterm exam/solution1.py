n=int(input())
m=list(map(int,input().split()))
d=list(map(int,input().split()))
x=int(input())

count = 0
sm = m[0]
bg = d[0]
for i in range(n):
    sm = max(sm, d[i])
    bg = min(bg, m[i])

for i in range(n):
    if (abs(m[i] - sm) > x or abs(m[i] - bg) > x):
        count += 1

print(count)

def fmid( n ):
    cnt = 0
    while n > 0:
        n =int(n/5)
        cnt += n

    return cnt

def test( n ):
    low = 0
    high = 5*n
    while low < high:
        mid = int((low + high) / 2)
        count = fmid(mid)
        if count < n:
            low = mid + 1
        else:
            high = mid
    print(low)

n = int(input())
test(n)

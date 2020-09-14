# 13458번 : 시험감독 - greedy
import sys

n = int(sys.stdin.readline().rstrip())
result = [-1 for i in range(n)]
a = list(map(int, input().split()))

b, c = map(int, sys.stdin.readline().rstrip().split())
cnt_ = 0
for i in range(n):
    #print("first", i)
    cnt = 0
    while True:
        if a[i] <= 0:
            break
        elif cnt == 0:
            a[i] -= b
            cnt += 1
        else:
            mod = a[i] % c
            #print(mod)
            #a[i] -= c
            div = (a[i] - mod)/c
            if mod == 0:
                cnt += div
            else:
                cnt += div+1
                #print(cnt)
            break
    #print("second", i)
    result[i] = cnt

cnt_ = sum(result)
print(int(cnt_))

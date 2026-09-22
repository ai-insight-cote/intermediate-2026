# 1이될때까지

N,K = map(int,input().split())
count = 0
#N = (N//K) * K #N이 K로 나누어떨어질 수 있는 제일 가까운 수
while N!=1:
    if N%K==0:
        N = N//K
    else:
        N-=1
    count+=1
print(count)
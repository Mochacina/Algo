n,m=map(int,input().split())
def f(a,b=[]):
 if a==m:print(*b);return
 [f(a+1,b+[sorted(list(map(int,input().split())))[i]])for i in range(n)]
f(0)
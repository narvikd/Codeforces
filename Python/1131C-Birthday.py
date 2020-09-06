#https://codeforces.com/problemset/problem/1131/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(inl())
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.insert(0, a[i])
    else:
        ans.append(a[i])
out(ans, " ")

#https://codeforces.com/contest/1650/problem/A

from pickle import FALSE
import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    s = ins()
    c = ins()
    print("YES" if c in s[0::2] else "NO")

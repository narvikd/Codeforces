#https://codeforces.com/problemset/problem/1352/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(k + (k-1) // (n-1))

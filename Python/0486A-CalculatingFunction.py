#https://codeforces.com/problemset/problem/486/A

n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    print((n//2 + 1) * -1)
n = int(input())
for i in range(0,10**9):
    a = 2**i
    if a > n:
        break
print(str(a))

def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

n = int(input())

if perfect_number(n):
    print("YES")
else:
    print("NO")
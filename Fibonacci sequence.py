def fibonacci(n):  

    FibArray = [0, 1]  
    while len(FibArray) < n + 1:  
        FibArray.append(0)  
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  

s = int(input())

list = []

for i in range(1, s+1):
    list.append(fibonacci(i))

for index in range(1, s+1):
    for j in list:
        if index == j:
            print('+', end='')
            f = 0
            break
        f = 1
    if f == 1:
        f = 0
        print('-',end='')

print()
            

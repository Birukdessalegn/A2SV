t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    possible = True
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n - 1):
        if arr[i+1] - arr[i] > 1:  
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")

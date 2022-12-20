i = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 15, 18]
n = len(arr)
print(n)
result = 0
while i < n:
    if arr[i] % 2 == 0:
        print(arr[i])
    i = i + 1

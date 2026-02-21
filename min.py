arr=[1,32,43,-13,42,0]

min_val=arr[0]

for i in range(1,len(arr)):
    if arr[i]<min_val:
        min_val=arr[i]


print(min_val)        
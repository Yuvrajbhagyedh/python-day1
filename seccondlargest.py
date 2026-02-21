arr=[10, 5, 8]

max_val=arr[0]
secondlargest=0

for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
    elif arr[i]<max_val and arr[i]>secondlargest:
          secondlargest=arr[i]



print(max_val)
print(secondlargest)                
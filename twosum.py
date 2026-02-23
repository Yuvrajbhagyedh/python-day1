arr=[1,2,3,4,5]

left=0
right=len(arr)-1
target=5

while left<right:
    curr_sum=arr[left]+arr[right]

   
    if curr_sum==target:
        print("target matched")
        break
    elif curr_sum>target:
        right-=1
    elif curr_sum<target:
        left+=1

        
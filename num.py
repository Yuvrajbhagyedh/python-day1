import numpy as np

lis=[1,2,3,4,5]
lis2=[2,4,5,56,3]
lis3=[2,4,5,56,3]
arr=np.array([lis,lis2,lis3])

arr1=arr.reshape(5,3)
print(arr1)
print(type(arr))

arr = "nvdfjfdfldl"
dict={}

for i in arr:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
    


print(dict)        
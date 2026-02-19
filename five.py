# dictionaries in python
dict1={
    "name":"Yuvraj K",
    "roll no":162,
    "marks":{
        "cn":89,
        "os":56
    }
}

#now taking input from the user for dictionaries

n=int(input("enter  the range "))
dict={}
for num in range(n):
    key=input("enter the value for key")
    value=input("enter the value")
    dict[key]=value


print(dict)
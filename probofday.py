#the first problem is to print form 1 to 20
n=int(input("enter the range to check even "))
total=0
for i in range(2,n+1):
   if(i%2==0):
      total+=1

print(total)   
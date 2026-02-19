num=int(int(input()))
origina=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10

if(rev==origina):
    print("palindrom")
else:
    print("not palindrom")
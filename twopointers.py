s="mada"
left=0
right=len(s)-1

ispalindrom=True
while left<right:
    if s[left]!=s[right]:
        ispalindrom=False
        break

    left+=1
    right-=1


if ispalindrom:
    print("the word is a palindrome")

else:
    print("not a palindrome")    
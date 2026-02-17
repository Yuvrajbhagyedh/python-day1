#conditional statements

a=int(input("enter your age"))

if(a==18):
    print("adult")
if(a>=45):
    print("parent")
else:
    print("dont know")    

    #problems on conditional statements
    #first one is even or odd we take input from the user and check user input is even or odd number

    inp=int(input("enter a number to check whether a number is even or odd"))
    if inp%2==0:
        print("even number")
    else:
        print("odd")    

        #Voting Eligibility

age=int(input("enter your to check whether you are eligible to vote or not"))
if age>=18 and age<=100:
            print("eligible to vote")
else:
            print("appi ning inna age agilla")    
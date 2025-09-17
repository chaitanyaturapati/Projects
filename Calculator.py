a=int(input("enter a number : "))
b=int(input("enter other number : "))
c = input("Enter operator (+, -, *, %, /): ")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="%":
    print(a%b)
elif c=="/":
    if b==0:
         print("Error: Division by zero is not allowed.") 
    else :
       print(a/b)
else:
    print("Invalid operator")




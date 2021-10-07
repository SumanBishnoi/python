#code with harry faulty calculator problem

operation= input("choose operation + for addition, * for multiplication, / for division=  ")
a= int(input("enter first no.="))
b= int(input("enter second no.="))
if a==56 and b==7 and operation=="+":
    print("77")
elif a==45 and b==3 and operation=="*":
    print("555")
elif a==56 and b==6 and operation=="/":
    print("4")
elif operation=="+":
        print(a+b)
elif operation=="*":
        print(a*b)
elif operation=="/":
     print(a/b)
else:
    print("invalid entry")

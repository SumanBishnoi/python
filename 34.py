def check1():
    x=20
    def check2():
        global x
        x=88
    print("before calling check2() ",x)
    check2()
    print("after calling check2() ",x)
    
check1()
print(x)

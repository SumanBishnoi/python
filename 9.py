def a(m1,m2,m3, m4=15000):
    total=m1+m2+m3
    if total>=m4:
        print("you can buy a smartphone")
    else:
        print("you can't buy a smartphone")

n1=int(input("enter your savings= "))
n2=int(input("enter your pocket money= "))
n3=int(input("enter your money earned= "))
a(n1,n2,n3)

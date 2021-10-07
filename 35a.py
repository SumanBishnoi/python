#fabniocci series

def fab_iterative(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabniocci(n-1)+fabniocci(n-2)

number= int(input("enter any number= "))
print(fab_iterative(number))
        
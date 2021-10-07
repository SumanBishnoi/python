#check whether a number is prime
num= int(input("enter a number= "))

for x in range(2,num):
    if num%x==0:
        print(" not a prime number")
        break
else:
    print("prime no.")
#factorial
num= int(input("enter a number= "))
fact=1
for x in range(1,num+1):
    fact= fact*x
print("the factorial of num{} is {}".format(num,fact))
    
#average of numbers in a list

total=0
list1=[10,20,30,40,50,60]

for n in list1:
    total=total+n
average=total/ len(list1)
print("average=", average)
#ifelse statement

year= int(input("input any year= "))

if year%100==0:
    if year%400==0:
        print("leap year")
elif year%4==0:
     print("leap year")
else:
     print("not a leap year ")


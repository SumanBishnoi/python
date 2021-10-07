#practice exercise- finding avg squats done in a week
#section1- define three variables
day=0
sqauts=0
total=0
print("enter the total no. of squats u did in the last week\n")

#section2
while day<=6:
    day=day+1
    sqauts=int(input("squats on day{}: ".format(day)))
    total=total+sqauts

#section3    
avg= total/day
print("in the last {} days, you did an average of {} squats!".format(day,avg))
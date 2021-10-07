def getdate():
    import datetime
    return datetime.datetime.now()

def get_client(x):
    client= x
    if client==1:
        action=int(input("Press 1 for exercise or 2 for diet= "))
        if action==1:
            add= int(input("Press 1 for log or 2 for retrieval= "))
            if add==1:
                a= input("Enter your exercise= ")
                with open("harry-ex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" +a+"\n")
                print("successfully added")
            elif add==2:
                 with open("harry-ex.txt") as af:
                     for i in af:
                         print(i, end="")
        elif action==2:
                add= int(input("Press 1 for log or 2 for retrieval= "))
                if add==1:
                    b= input("Enter your diet= ")
                    with open("harry-dt.txt","a") as f:
                     f.write(str([str(getdate())]) + ":" +b+"\n")
                    print("successfully added")
                elif add==2:
                        with open("harry-dt.txt") as af:
                            for i in af:
                             print(i, end="")



    if client==2:
        action=int(input("Press 1 for exercise or 2 for diet= "))
        if action==1:
            add= int(input("Press 1 for log or 2 for retrieval= "))
            if add==1:
                a= input("Enter your exercise= ")
                with open("rohan-ex.txt","a") as f:
                    f.write(str([str(getdate())]) + ":" +a+"\n")
                print("successfully added")
            elif add==2:
                 with open("rohan-ex.txt") as af:
                     for i in af:
                         print(i, end="")
        elif action==2:
                add= int(input("Press 1 for log or 2 for retrieval= "))
                if add==1:
                    b= input("Enter your diet= ")
                    with open("rohan-dt.txt","a") as f:
                     f.write(str([str(getdate())]) + ":" +b+"\n")
                    print("successfully added")
                elif add==2:
                        with open("rohan-dt.txt") as af:
                            for i in af:
                                print(i, end="")

    if client==3:
        action=int(input("Press 1 for exercise or 2 for diet= "))
        if action==1:
            add= int(input("Press 1 for log or 2 for retrieval= "))
            if add==1:
                a= input("Enter your exercise= ")
                with open("hammad-ex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ":" +a+"\n")
                print("successfully added")
            elif add==2:
                 with open("hammad-ex.txt") as af:
                     for i in af:
                         print(i, end="")
        elif action==2:
                add= int(input("Press 1 for log or 2 for retrieval= "))
                if add==1:
                    b= input("Enter your diet= ")
                    with open("hammad-dt.txt", "a") as f:
                     f.write(str([str(getdate())]) + ":" +b+"\n")
                    print("successfully added")
                elif add==2:
                        with open("hammad-dt.txt") as af:
                            for i in af:
                             print(i, end="")

print("Welcome to the Health Management System")
name= int(input(" choose cleint- press 1 for harry, 2 for Rohan and 3 for hammad= "))
svs= get_client(name)

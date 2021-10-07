import random

def game(n):
    choice= n
    comp= random.choice("swg")
    if n==comp:
        print("Tie, try again")
    elif n=='s' and comp=='w':
        print("you win")
    elif n=='s' and comp=='g':
        print("you lose")
    elif n=='w' and comp=='s':
        print("you lose")
    elif n=='w' and comp=='g':
        print("you win")
    elif n=='g' and comp=='s':
        print("you win")
    elif n=='g' and comp== 'w':
        print("you lose")
    






print("Let's Play")
n=1
while n<=10:
    print("enter your choice s/w/g= ")
    a=input()
    game(a)
    print("total over chances= ",n)
    n=n+1
    
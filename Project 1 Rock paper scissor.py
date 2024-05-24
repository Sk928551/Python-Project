import random
p1=int(input("choose one of the following: 1.Rock 2.paper 3.scissors"))
p2=random.randint(1,3)

if p1==1 and p2==3:
    print("You are   the winner" )
elif p1==2 and p2==1:
    print("You  are the winner")

elif p1==3 and p2==2:
    print("You are  the winner")

elif p1==p2:
    print("It's match draw")

else:
    print("Computer  is the winner")

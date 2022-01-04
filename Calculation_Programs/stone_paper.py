import random
print("Welcome to the Game Stone Paper""&"" Scisssor \n Stone\n Scissor\n Paper")
tournament=int(input("Enter how many times you want to play : "))
User1=['Stone','Paper','Scissor']
count=0
count1=0
i=0
for i in range(tournament):
    User2=input("Enter Your Choice For User1: ")
    x=random.choice(User1)
    print(x)
    if (x=='Stone' and User2=='Paper') or x=='Paper' and User2=='Scissor' or x=='Scissor' and User2=='Stone'  :
        print("User1 Wins....")
        count=count+1
    elif x=='Paper' and User2=='Stone' or x=='Scissor' and User2=='Paper' or x=='Stone' and User2=='Scissor':
        print("Computer Wins....")
        count1=count+1
    elif x==User2:
        print("Draw OR Tie")
    else:
        print("You have not entered Valid Choice OR Enter the choice Having First character Capital")
if count>count1:
    print("\n user wins")
elif count==count1:
    print("\ndraw")
else:
    print("\ncomputer wins")



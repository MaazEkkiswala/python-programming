n=int(input("How many team="))
team1=[]
team=''
name=input("Enter team name=")
if name =='csk' or name =='rcb' or name =='rr' or name =='mi' or name =='pun':
    for i in range(n):
        win=int(input("how many match won="))
        if win>2 and win<5:
            print("qualified")
            team1.append(name)
        else:
            print("Not qualified")
print(team1)

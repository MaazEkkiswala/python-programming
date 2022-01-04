n=int(input("How many team="))
team=[]
for i in range(n):
    name=input("Enter team name=")
    win=int(input("how many match won="))
    if win>2 and win<5:
        print("qualified")
        team.append(name)
    else:
        print("Not qualified")
print(team)


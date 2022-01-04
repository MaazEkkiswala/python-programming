id=1234
class Atm():
    # id = int(input("\nEnter account pin: "))
    # while id < 1000 or id > 9999:
    #     id =int(input("\nInvalid Id.. Re-enter: "))

    def balance(self,a):
        self.a=a
        return self.a

    def deposit(self):
         d=int(input("enter amount to deposiyted:"))
         self.a+=d
         return self.a

    def withdraw(self):
         d=int(input("enter amount to withdraw:"))
         self.a-=d
         return self.a
x1=Atm()
trail=3
choice=0
x=int(input("SET PIN="))
print(x)
while True:
    y=int(input("Enter the PIN that you have set before="))
    if y==x:
         print("Enter choice 1=To see balance , 2=Deposit , 3=Withdraw=")
         choice=int(input("Enter choice="))
         if choice==1:
             print(x1.balance(5000))
         if choice==2:
             print(x1.balance(5000))
             print("Updated Balance=",x1.deposit())
         if choice==3:
             print(x1.balance(5000))
             print("Updated Balance",x1.withdraw())
    else:
          print("Enter valid pin")
          trail=trail-1
          if trail==0:
             print("Your card is blocked")
          else:
             print("Your trail left",trail) 
    

  


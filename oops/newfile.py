class ATM():
    def balance(self,a):
        self.a=a
        return self.a
    def deposite(self):
        d=int(input("Enter Deposite ammount... "))
        self.a+=d
        return self.a
    def withdraw(self):
        d=int(input("Enter The Withdraw ammount.."))
        self.a-=d
        return self.a
#setup from user...
x= ATM()
n=int(input("set the balaance.."))
print(x.balance(n))
b=int(input("SET pin"))
phon_no = int(input("enter mobile number.."))
trial = 3
while True:
    pin=int(input("enter the pin TO do transactions.."))
    if pin ==b :
        user_input=int(input("1. To SET pin,2. TO deposite ammount, 3. TO WIthdraw ammount,4.TO END TRANSACTION"))
        
        if user_input ==1:
                while True :
                     current_pin=int(input("enter the current pin..."))
                     if b == current_pin:
                         print("working....")
                         break
                     else :
                         trial= trial -1
                         if trial == 0:
                             print("your card is blocked")
                             break
                         else:
                             print("you left ",trial,"trial")
                             print("INVALID PIN...")
                             
                        


        
        elif user_input ==2 :
                while True:
                     pin=int(input("enter the pin.."))
                     if pin ==b:
                          print("UPDATED BALANCE = ",x.deposite())
                          break  
                     else:
                         trial= trial -1
                         if trial == 0:
                             print("your card is blocked")
                             break
                         else:
                              print("you left ",trial,"trial")
                              print("INVALID PIN...") 
                               

        
        
        elif user_input == 3:
                while True:
                     pin=int(input("enter the pin.."))
                     if pin ==b:
                         print("UPDATED BALANCE = ",x.withdraw())   
                     else:
                         trial= trial -1
                         if trial == 0:
                             print("your card is blocked")
                             break
                         else:
                             print("you left ",trial,"trial")
                             print("INVALID PIN...")  

        
        elif user_input == 4:
                break
        
        else:
            print("INVALID..")
    
   
    else:
         trial= trial -1
         if trial == 0:
             print("your card is blocked")
             break
         else:
             print("you left ",trial,"trial")
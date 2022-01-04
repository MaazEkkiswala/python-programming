class Atm():
    id = int(input("\nEnter account pin: "))
    while id < 1000 or id > 9999:
        id =int(input("\nInvalid Id.. Re-enter: "))
    if id==1234:
        print("ok")
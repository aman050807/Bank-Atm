class Atm:
     def __init__(self,cardnumber,pin):
         self.cardnumber=cardnumber
         self.pin=pin

def check_balance(self):
    print("Your balance is 10,00,000")

def withdrawal(self,amount):
    newamount=10,00,000-amount
    print("you have withdrawn "+str(amount)+"your remaining balance is "+str(newamount))

def main():
    cardnumber=input("insert your card number:- ")
    pinnumber=input("enter your pin number:-")
    newuser=Atm(cardnumber,pinnumber)

    print("choose your activity")
    print("1.Balance Enquriy  2.Withdrawal")
    activity=int(input("entre activity number:- "))

    if (activity == 1):
         newuser.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        newuser.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()

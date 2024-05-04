import random

def userInfo(): #get the user's info
    while True:
        name = input("What is your name? " )
        balance = input("How much would you like to deposit: $")
        if isinstance(name, str) and balance.isdigit():
            break
        print("nigga you done fucked something up") 
        
    return name, balance

def betInfo(balance): #gets the users bet amount and choice of bet
    while True:
        betAmount = input("Select betting amount: ")
        betChoice = input("Pick a color (r/b) or number(1-36): ")
        

        if betChoice.isdigit() or isinstance(betChoice, str) and betAmount.isdigit():
            if betChoice == 'r' or 'b' or 0 <= betChoice <= 36 and betAmount <= balance:
                break
            
        print("your betting choice is out of acceptable range, try again")
    
    return betChoice, betAmount

def spinResult(): #use random module to get results
    num = (random.randrange(0, 36))
    while True:
        if (num == 0):
            color = "g"
            break
        elif (num % 2) == 0:
            color = "b"
            break
        elif (num % 2) == 1:
            color = "r"
            break
        
    return num, color
    
def winningChecker(num, color, betChoice, betAmount, balance): #winning and new balance checker
    
    if (color == betChoice):
        print("you picked the right color")
        balance = balance + (betAmount*2)
    elif (num == betChoice):
        print("you picked the right number")
        balance = balance + (betAmount*35)
    else:
        print("nigga u lost")
        balance = balance - (betAmount)
        
    return balance


def main():
    name, balance = userInfo()
    betChoice, betAmount = betInfo(balance)
    num, color = spinResult()
    newBalance = winningChecker(num, color, betChoice, betAmount, balance)
    
    print("Name: ", name)
    print("Balance: ", balance)
    
    print("Bet Color: ", betChoice)
    print("Bet Amount: ", betAmount)
    
    print("Resulting Number: ", num)
    print("The color: ", color)
    
    print("Your new Balance is: ", newBalance)

main()


print("Hello, this is bank system")
balance = 0
while True:
    choice = input('Choose an option 1: Deposit, 2: Withdraw, 3: Quit  -   ')
    if choice=="1" or choice=="deposit" or  choice=="Deposit":
        addition=int(input('Enter the amount to deposit: '))
        balance+=addition
        print("Your balance is: {}".format(balance))
    elif choice=="2" or choice=="withdraw" or choice=="Withdraw":
        subtraction=float(input('Enter the amount to withdraw: '))
        if balance<subtraction:
            print('Your withdraw amount is greater than your balance.')
        else:
            balance-=subtraction
            print("Your balance is: {}".format(balance))
    elif choice=="3" or choice=="quit" or choice=="Quit":
        print('Exit')
        break
    else:
        print('Invalid input')
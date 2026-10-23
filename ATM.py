print("Welcome to Atm counter")

balance = 100

run_code = True

while run_code:

    options = ["1.show balance", "2.withdraw", "3.deposit"]
    print(options)

    ask = int(input("How we can help you Sir/Ma'am?"))

    match ask:

        case 1:
            print(f"This is your balance: {balance}:")
            more = input("Would you like to continue?")

            if more == "yes":
                run_code = True
            else :
                run_code = False
        case 2:
            cash = int(input("How much amount you want to withdraw?"))
            balance = balance - cash
            print(balance)
            more = input("Would you like to continue?")
            
            if more == "yes":
                run_code = True
            else :
                run_code = False

        case 3:
            money = int(input("How much amount you want to deposit?"))
            balance = balance + money
            print(balance)
            more = input("Would you like to continue?")
                        
            if more == "yes":
                run_code = True
            else :
                run_code = False


print("Thank you very much , bank is very poor!!!")

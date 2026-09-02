import random


# ==========================================
# STARTING VARIABLES
# ==========================================

balance = 0
warning_shown = False


print("========================================")
print("          WELCOME TO IAA SLOTS")
print("========================================")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n========================================")
    print("             CHOOSE YOUR SLOT")
    print("========================================")
    print("Balance: $", balance)
    print()
    print("1. Number Slot")
    print("2. Symbol Slot")
    print("3. Deposit")
    print("4. Cash Out")
    print("0. Exit")

    choice = input("\nEnter option: ")


    # ======================================
    # NUMBER SLOT
    # ======================================

    if choice == "1":

        while True:

            print("\n========================================")
            print("              NUMBER SLOT")
            print("========================================")
            print("Balance: $", balance)
            print()
            print("1. Spin Now")
            print("0. Back")

            option = input("\nEnter option: ")

            if option == "1":

                if balance <= 0:
                    print("\nYou do not have enough money.")
                    print("Go back and make a deposit first.")
                    continue

                try:
                    bet = int(input("\nEnter your bet: $"))

                    if bet <= 0:
                        print("\nInvalid bet.")
                        print("Your bet must be greater than $0.")

                    elif bet > balance:
                        print("\nYou do not have enough balance.")

                    else:

                        balance = balance - bet

                        print("\nSpinning...")

                        number1 = random.randint(1, 5)
                        number2 = random.randint(1, 5)
                        number3 = random.randint(1, 5)

                        print("\n========================================")
                        print("              RESULTS")
                        print("========================================")

                        print()
                        print("        ", number1, "|", number2, "|", number3)
                        print()

                        if number1 == number2 and number2 == number3:

                            winnings = bet * 5
                            balance = balance + winnings

                            print("JACKPOT!")
                            print("All 3 numbers matched!")
                            print("You won $", winnings)

                        elif (
                            number1 == number2
                            or number1 == number3
                            or number2 == number3
                        ):

                            winnings = bet * 2
                            balance = balance + winnings

                            print("YOU WON!")
                            print("2 numbers matched!")
                            print("You won $", winnings)

                        else:

                            print("You lost.")
                            print("Try again!")

                        print("\nUpdated Balance: $", balance)

                        if balance >= 100000 and warning_shown == False:

                            print("\n========================================")
                            print("     YOU HAVE REACHED $100,000!")
                            print("========================================")
                            print("We recommend that you stop")
                            print("playing for today.")
                            print()
                            print("You may continue if you want.")

                            warning_shown = True

                except ValueError:
                    print("\nPlease enter a valid number.")

            elif option == "0":
                break

            else:
                print("\nInvalid option.")


    # ======================================
    # SYMBOL SLOT
    # ======================================

    elif choice == "2":

        symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣", "🍀"]

        while True:

            print("\n========================================")
            print("              SYMBOL SLOT")
            print("========================================")
            print("Balance: $", balance)
            print()
            print("1. Spin Now")
            print("0. Back")

            option = input("\nEnter option: ")

            if option == "1":

                if balance <= 0:
                    print("\nYou do not have enough money.")
                    print("Go back and make a deposit first.")
                    continue

                try:
                    bet = int(input("\nEnter your bet: $"))

                    if bet <= 0:
                        print("\nInvalid bet.")
                        print("Your bet must be greater than $0.")

                    elif bet > balance:
                        print("\nYou do not have enough balance.")

                    else:

                        balance = balance - bet

                        print("\nSpinning...")

                        symbol1 = random.choice(symbols)
                        symbol2 = random.choice(symbols)
                        symbol3 = random.choice(symbols)

                        print("\n========================================")
                        print("              RESULTS")
                        print("========================================")

                        print()
                        print("        ", symbol1, "|", symbol2, "|", symbol3)
                        print()

                        winnings = 0

                        # ==================================
                        # THREE SYMBOLS MATCH
                        # ==================================

                        if symbol1 == symbol2 and symbol2 == symbol3:

                            if symbol1 == "7️⃣":

                                winnings = bet * 10

                                print("🎰 MEGA JACKPOT! 🎰")
                                print("7️⃣ | 7️⃣ | 7️⃣")
                                print("You won 10X your bet!")

                            elif symbol1 == "💎":

                                winnings = bet * 8

                                print("💎 BIG WIN! 💎")
                                print("Triple Diamonds!")
                                print("You won 8X your bet!")

                            elif symbol1 == "🔔":

                                winnings = bet * 6

                                print("🔔 GREAT WIN! 🔔")
                                print("Triple Bells!")
                                print("You won 6X your bet!")

                            elif symbol1 == "🍒":

                                winnings = bet * 5

                                print("🍒 NICE WIN! 🍒")
                                print("Triple Cherries!")
                                print("You won 5X your bet!")

                            elif symbol1 == "🍀":

                                winnings = bet * 5

                                print("🍀 LUCKY WIN! 🍀")
                                print("Triple Clovers!")
                                print("You won 5X your bet!")

                            elif symbol1 == "🍋":

                                winnings = bet * 4

                                print("🍋 YOU WON! 🍋")
                                print("Triple Lemons!")
                                print("You won 4X your bet!")

                            balance = balance + winnings

                            print("You won $", winnings)

                        # ==================================
                        # TWO SYMBOLS MATCH
                        # ==================================

                        elif (
                            symbol1 == symbol2
                            or symbol1 == symbol3
                            or symbol2 == symbol3
                        ):

                            winnings = bet * 2

                            balance = balance + winnings

                            print("🎉 YOU WON! 🎉")
                            print("2 symbols matched!")
                            print("You won 2X your bet!")
                            print("You won $", winnings)

                        # ==================================
                        # NO MATCH
                        # ==================================

                        else:

                            print("😢 You lost.")
                            print("Try again!")

                        print("\nUpdated Balance: $", balance)

                        if balance >= 100000 and warning_shown == False:

                            print("\n========================================")
                            print("     YOU HAVE REACHED $100,000!")
                            print("========================================")
                            print("We recommend that you stop")
                            print("playing for today.")
                            print()
                            print("You may continue if you want.")

                            warning_shown = True

                except ValueError:
                    print("\nPlease enter a valid number.")

            elif option == "0":
                break

            else:
                print("\nInvalid option.")


    # ======================================
    # DEPOSIT
    # ======================================

    elif choice == "3":

        print("\n========================================")
        print("                DEPOSIT")
        print("========================================")

        print("Current Balance: $", balance)
        print()
        print("Minimum Deposit: $100")
        print("Maximum Deposit: $20,000")

        try:
            deposit = int(input("\nEnter deposit amount: $"))

            if deposit < 100:

                print("\nInvalid amount.")
                print("Minimum deposit is $100.")

            elif deposit > 20000:

                print("\nInvalid amount.")
                print("Maximum deposit is $20,000.")

            else:

                balance = balance + deposit

                print("\nDeposit successful!")
                print("You deposited: $", deposit)
                print("New Balance: $", balance)

                if balance >= 100000 and warning_shown == False:

                    print("\n========================================")
                    print("     YOU HAVE REACHED $100,000!")
                    print("========================================")
                    print("We recommend that you stop")
                    print("playing for today.")
                    print()
                    print("You may continue if you want.")

                    warning_shown = True

        except ValueError:
            print("\nPlease enter a valid number.")


    # ======================================
    # CASH OUT
    # ======================================

    elif choice == "4":

        print("\n========================================")
        print("               CASH OUT")
        print("========================================")

        print("Current Balance: $", balance)

        if balance == 0:

            print("\nYou do not have any money to cash out.")

        else:

            print("\nAre you sure you want to cash out?")
            print("1. Yes")
            print("0. No")

            cash_choice = input("\nEnter option: ")

            if cash_choice == "1":

                print("\nCash out successful!")
                print("You cashed out: $", balance)

                balance = 0

                print("New Balance: $", balance)

            elif cash_choice == "0":

                print("\nCash out cancelled.")

            else:

                print("\nInvalid option.")


    # ======================================
    # EXIT PROGRAM
    # ======================================

    elif choice == "0":

        print("\n========================================")
        print("      THANK YOU FOR USING IAA SLOTS")
        print("========================================")

        break


    # ======================================
    # INVALID OPTION
    # ======================================

    else:

        print("\nInvalid option.")
        print("Please choose 0, 1, 2, 3, or 4.")


print("\nProgram stopped.")

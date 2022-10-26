"""The challenge is to write code using an IF statement.
This program will read your mind and know which number you are thinking of.
The questions are not clear enough, so I am sorry about that.
Feel free to use the code as an example of IF statements in any material.
Just remember to refer to my Git Hub profile."""

# A while loop to try again
while True:

    print("I am about to read your mind. Pick a nmuber from 1 to 10!", "\n")
    input("When you are ready press Enter!")

    oddOrEven = input("Is your odd or even? ( o / e ):")

#Start to guess the odd number

    if oddOrEven == 'o':
        print("\n", "Divide your number by 2!")

        oinput1 = input("Is the result equal to or less than 2.5? ( y / n ):")

        if oinput1 == 'n':
            print("\n", "Now add 2 to your original number!")

            oinput2 = input("Is the result equal to or greater than 11? ( y / n ):")

            if oinput2 == 'y':
                print("\n", "Your number is: 9")

            else: print("\n", "Your number is: 7")

        if oinput1 == 'y':
            print("\n", "Now add 2 to your original number!")

            oinput3 = input("Is the result less than 7? ( y / n ):")

            if oinput3 == 'n':
                print("\n", "Your number is: 5")

            if oinput3 == 'y':
                print("\n", "Subtract 1 from your original number!")
    
                oinput4 = input("Is the result less than two? ( y / n ):")
                
                if oinput4 == 'y':
                        print("\n", "Your number is: 1")

                else:
                        print("\n", "Your number is: 3")

#Start to guess the even numer

    if oddOrEven == 'e':
        print("\n", "Divide your number by 2!")

        einput1 = input("Is the result equal to or less than 3? ( y / n ):")

        if einput1 == 'n':
            print("\n", "Now add 2 to your original number!")

            einput2 = input("Is the result equal to or greater than 12? ( y / n ):")

            if einput2 == 'y':
                print("\n", "Your number is: 10")

            else: print("\n", "Your number is: 8")

        if einput1 == 'y':
            print("\n", "Now add 2 to your original number!")

            einput3 = input("Is the result less than 8? ( y / n ):")

            if einput3 == 'n':
                print("\n", "Your number is: 6")

            if einput3 == 'y':
                print("\n", "Subtract 2 from your original number!")
    

                einput4 = input("Is the result less than two? ( y / n ):")
    
                if einput4 == 'y':
                    print("\n", "Your number is: 2")

                else:
                    print("\n", "Your number is: 4")

#Asking the user if they want to try again
                    
    again = input("Do you want to try again? ( y / n ):")

    if again == 'y':

        continue

    else:

        break

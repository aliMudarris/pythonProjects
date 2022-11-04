#This code calculates a user's BMI using pounds and inches

#A while loop to ask the user if they want to try again

while True:

    #Asking the user to enter their weight and height

    weight = float(input("Enter your wheight in (lb): "))
    height = float(input("Enter your height in (in): "))

    #A function to calculate the BMI and return the result

    def bmiCal(w, h):

        return w / (h **2) * 703

    result = bmiCal(weight, height)

    #Printing the result

    print("Your BMI is: ", round(result,1))

    #BMI Categories

    if result < 18.5: print("You are underweight.")
    elif result >= 18.5 and result <= 24.9: print("Your wheight is normal.")
    elif result >= 25.0 and result <= 29.9: print("You are overweight.")
    elif result >= 30.0: print("You are obese.")

    #Ask the user if they want to try again
    
    tryAgain = input("Do you want to try again? ( y / n): ")

    if tryAgain == 'y':

        continue

    else:

        break

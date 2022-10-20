import random

#Loop to try different numbers
while True:

  #The rang of the Lottery numbers  
    NumOne = int(1)
    NumTwo = int(69)

    x = [random.randint(NumOne,NumTwo) for i in range(5)] 
    y = [random.randint(NumOne,NumTwo) for i in range(1)]
    
    print("Yoyr Lottery Numbers are: ", x, "PBall number is: ", y)

    #Ask the user if want to try another set of numbers

    nNum = input("Do you like to try another set of numbers? (y/n): ")
    if nNum =='y':
        continue
    else:
        break

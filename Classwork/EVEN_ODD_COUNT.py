secret =float(input("enter a number to guess:\n"))
guess = 0

while guess != secret:
    guess = float(input("Guess (1-10): "))
    if guess < secret:
       print("Too low")
    elif guess > secret:
       print("Too High")
    else:
        print("Correct!")
           
    


    
            
    

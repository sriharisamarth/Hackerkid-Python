number=int(input("Enter a number to check the factorial of:\n"))

factorial = 1

i = 1

if number <0:
    print("The program doesnt work for negative number")
    
elif number ==0:
    print("The factorial of 0 is 1")
else:
    while i <= number:
        factorial *= i
        i = i + 1
    print(f"The factorial of {number} is {factorial}")
    

    

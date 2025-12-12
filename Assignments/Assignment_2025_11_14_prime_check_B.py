x=int(input("Enter a number:\n"))

y=int(x/2)

for i in range(2,y):
    if x%i==0:
        print(x,"is not a prime number")
        break
        
    else:
        print(x,"is a prime number")
        break

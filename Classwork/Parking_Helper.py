print("Parking check")
hrs = float(input("Hours Parked: "))

if hrs <=2:
    print("Fee =",(2 * 20)+(hrs-2)*50)
elif hrs <=5:
    print("Fee =",(2 * 20)+(hrs - 20)* 50)
else:
    print("Fee =",(2 * 20)+(3*50)+(hrs - 5) * 100)



######################################
print("Next one Electricity check")


units = int(input("Enter units: \n"))


if units <= 100:
    bill=units * 5
elif units <= 200:
    bill = (100*5)+(units - 100) * 7
else:
    bill =(100 * 5)+(100 * 7)+(units - 200)*10

print("Total Bill=",bill)

########################################
print("Next one Mark Check")

m1 = int(input("Enter The first number:\n"))
m2 = int(input("Enter The second number:\n"))
m3 = int(input("Enter The third number:\n"))


avg = (m1 + m2 + m3)/3

if m1 < 40 or m2 < 40 or m3 <40:
    print("Fail (One subject below 40)")
elif avg>=75:
    print("Distinction")
elif avg>=60:
    print("First class")
elif avg>=50:
    print("Second class")
else:
    print("Pass")




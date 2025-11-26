car={"name":"Ford","Type":"SUV","Fuel_Type":"Diesel"}

print(car)
print(car["name"])
print(car["Type"])

print(car.get("Type"))
car["Type"]="Sedan"
car["Fuel_Type"]="Petrol"

print(car)

print("Next One")

animal={"name":"Cow","Type":"Mammal","Resource":"Milk"}

print(animal)
print(animal["name"])
print(animal["Type"])

print(animal.get("Type"))
animal["Type"]="Dairy_Cattle"
animal["Resource"]="Fertillizer"

print(animal)

print("Next One")


smartphone={"name":"Iphone","OS":"IOS","Manufacturer":"Apple"}

print(smartphone)
print(smartphone["name"])
print(smartphone["OS"])

print(smartphone.get("OS"))
smartphone["OS"]="Android"
smartphone["Manufacturer"]="Samsung"

print(smartphone)

print("Next One")

pen={"color":"Blue","Type":"Gel","Manufacturer":"Parker"}

print(pen)
print(pen["color"])
print(pen["Type"])

print(pen.get("Manufacturer"))
pen["Type"]="Ball Pen"
pen={"color":"Blue","Type":"Gel","Manufacturer":"Parker"}

print(pen)
print(pen["color"])
print(pen["Type"])


print(pen.get("Manufacturer"))
pen["Type"]="Ball Pen"
print(pen)

print("Next One")
sport={"Name":"Cricket","Role":"Bowling","Overs":"50 Overs"}

print(sport)
print(sport["Name"])
print(sport["Role"])

print(sport.get("Manufacturer"))
sport["Name"]="Football"
sport["Role"]="Forward"
sport["Overs"]="90 minutes"
print(sport)




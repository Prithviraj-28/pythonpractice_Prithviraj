print("-------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------Ticket Pricing Software--------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")
print("Enter your age: ")
age = int(input())

if (age <= 5):
    print ("Your ticket is free")

elif(age>5 & age<=18):
    print("Ticket price : 900")

elif (age>18 and age<=40):
    print("Ticket price : 1200")

elif (age>40 and age<=70):
    print("Ticket price : 700")

else:
    print("invalid age")
    
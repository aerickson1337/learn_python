#Kyo Coffee Shop
#Robot Barista edition #1 

print("Hello, Welcome to Kyo's Coffee Shop!")

name = input("What is your name?\n")

if name == "Ben" or "Maia" or "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("Intruder!!!! Get out " + name)
    exit()

else:
    print (f"Hello {name} thanks for coming in!" )

menu = "Black Coffee, Espresso, Latte, Cappucino"

print(name + " , what would you like to order today? Here is what we are serving.\n" + menu)

order = input()

if order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    whipcream = input("Would you like whip cream with that?\n")
    if whipcream == "Yes":
        price = 9
        print("Perfect! With whip cream that'll be an extra $2")
    else:
        price = 7

elif order == "Cappucino":
    price = 8
else:
    print("Sorry, we don't have that here.")

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print ("Sounds good " + name + " we'll have your " + quantity + " " + order + "s ready for you in a few minutes. That'll be " + "$" + str(total) + " dollars.")

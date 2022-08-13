#Kyo Coffee Shop
#Robot Barista edition #1 

def check_if_customer_is_evil(name: str = None):
    known_evil_customers = ["Ben", "Maia", "Loki"]
    if name in known_evil_customers:
        evil_status = input("Are you evil?\n")
        good_deeds = int(input("How many good deeds have you done today?\n"))
        if evil_status == "Yes" and good_deeds < 4:
            print(f"Intruder!!!! Get out {name}")
        exit()
    print (f"Hello {name} thanks for coming in!" )

def _get_sanitized_input(input_text: str = None):
    if not input_text:
        return input()
    customer_input = input(input_text)
    return customer_input.lower().strip()

def main():
    print("Hello, Welcome to Kyo's Coffee Shop!")

    name = _get_sanitized_input("What is your name?\n")

    check_if_customer_is_evil(name)

    menu: list = ["Black Coffee", "Espresso", "Latte", "Cappucino"]

    welcome_text = (
        f"{name}, what would you like to order today?"
        "Here is what we are serving:" 
    )

    print(welcome_text)
    print('\n'.join(menu))

    order = _get_sanitized_input()

    if order == "Black Coffee".lower():
        price = 3
    elif order == "Espresso".lower():
        price = 5
    elif order == "Latte".lower():
        whipcream = _get_sanitized_input("Would you like whip cream with that?\n")
        if whipcream == "yes":
            still_wants_whipcream = _get_sanitized_input("It's two more dollars is that ok?\n")
            if still_wants_whipcream == "yes":
                price = 9
                print("Perfect! I'll get right on that")
            else:
                price = 7
        else:
            price = 7
    elif order == "Cappucino".lower():
        price = 8
    else:
        print(f"Sorry, we don't have {order} here.")

    quantity = _get_sanitized_input("How many coffees would you like?\n")

    total = price * int(quantity)

    goodbye_text = (
       f"Sounds good {name} we'll have your {quantity} {order}s "
       f"ready for you in a few minutes. That'll be {total} dollars." 
    )
    print (goodbye_text)

if __name__ == "__main__":
    main()
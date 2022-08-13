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

    welcome_text = (
        f"{name}, what would you like to order today? "
        "Here is what we are serving:" 
    )

    menu_dict = {
        0: {
            "name": "Black Coffee",
            "price": 3,
            "offer_whipped_cream": False,
        },
        1: {
            "name": "Espresso",
            "price": 5,
            "offer_whipped_cream": False,
        },
        2: {
            "name": "Latte",
            "price": 7,
            "offer_whipped_cream": True,
        },
        3: {
            "name": "Cappucino",
            "price": 8,
            "offer_whipped_cream": False,
        }
    }

    print(welcome_text)
    for order_number, menuitem in menu_dict.items():
        print(f"{order_number}) {menuitem.get('name')}")

    order = _get_sanitized_input()
    order_number = int(order)

    if order_number in menu_dict:
        menu_item = menu_dict[order_number]
        price = menu_item['price']
        if menu_item['offer_whipped_cream']:
            wants_whipped_cream = _get_sanitized_input("Would you like whip cream with that?\n")
            if wants_whipped_cream:
                still_wants_whipcream = _get_sanitized_input("It's two more dollars is that ok?\n")
                if still_wants_whipcream:
                    price = price + 2
    else:
        print(f"Sorry, we don't have {order} here.")

    quantity = _get_sanitized_input("How many coffees would you like?\n")

    total = price * int(quantity)

    goodbye_text = (
       f"Sounds good {name} we'll have your {quantity} {menu_dict[order_number]['name']}s "
       f"ready for you in a few minutes. That'll be {total} dollars." 
    )
    print (goodbye_text)

if __name__ == "__main__":
    main()
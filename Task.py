products = []


def read_data():
    open_file = open("Session_08/test2.txt", "r")

    for p in open_file:
        product = p.split(",")
        dic = {"id": int(product[0]), "name": product[1],
               "price": int(product[2]), "count": int(product[3])}
        products.append(dic)


def show_menu():
    print("1- Show Products")
    print("2- Add")
    print("3- Delete")
    print("4- Edit")
    print("5- Search")
    print("6- Buy")
    print("7- Exit")

    user_choice = int(input("enter your choice: "))

    while True:
        if user_choice == 1:
            show_products()
            back_to_menu()
            break
        elif user_choice == 2:
            add()
            back_to_menu()
            break
        elif user_choice == 3:
            delete()
            back_to_menu()
            break
        elif user_choice == 4:
            edit()
            back_to_menu()
            break
        elif user_choice == 5:
            search()
            back_to_menu()
            break
        elif user_choice == 6:
            buy()
            back_to_menu()
            break
        else:
            exit()
            break


def back_to_menu():
    show_menu_item = input("Enter 'b' to back to the menu: ")
    if show_menu_item == "b":
        show_menu()


def show_products():
    print(" id \t   name \t price \t\tcount")
    for product in products:
        print(product["id"], "\t", product["name"], "\t",
              product["price"], "\t\t", product["count"])


def add():
    id = input("Enter id: ")
    name = input("Enter name: ")
    price = int(input("Enter price: "))
    count = int(input("Enter count: "))

    for product in products:
        if id == str(product["id"]):
            print(f"A product with ID {id} already exists.")
            add()
            return
        elif name == str(product["name"]):
            print(f"A product with name {name} already exists.")
            add()
            return

    dic = {"id": int(id), "name": name, "price": price, "count": count}
    products.append(dic)
    print("Product added successfully!")
    show_products()


def delete():
    id_to_delete = int(
        input("Enter the ID of the product you want to delete: "))

    for product in products:
        if id_to_delete == int(product["id"]):
            products.remove(product)
            print(f"Product with ID {id_to_delete} has been deleted.")
            show_products()
            return

    print(
        f"Product with ID {id_to_delete} does not exist. Please choose another ID.")
    delete()


def edit():
    id_to_edit = input("Enter the ID of the product you want to edit: ")

    for product in products:
        if id_to_edit == str(product["id"]):
            print(f"Current values of product with ID {id_to_edit}:")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Count: {product['count']}")
            print("1- Name")
            print("2- Price")
            print("3- Count")
            item_to_edit = int(
                input("Please enter the number of the item you want to edit: "))

            if item_to_edit == 1:
                new_name = input("Enter the new name: ")
                product["name"] = new_name
                print(
                    f"The name of the product with ID {id_to_edit} has been updated to {new_name}.")
            elif item_to_edit == 2:
                new_price = int(input("Enter the new price: "))
                product["price"] = new_price
                print(
                    f"The price of the product with ID {id_to_edit} has been updated to {new_price}.")
            elif item_to_edit == 3:
                new_count = int(input("Enter the new count: "))
                product["count"] = new_count
                print(
                    f"The count of the product with ID {id_to_edit} has been updated to {new_count}.")
            break
    else:
        print(f"Product with ID {id_to_edit} is not in the products.")
        return

    print("Product updated successfully!")
    show_products()


def search():
    show_products()

    key = input("Enter your key: ")
    for product in products:
        if key == str(product["id"]) or key == product["name"]:
            print(product)
            break
    else:
        print("Not found")


def buy():
    cart = []
    while True:
        id_to_buy = input(
            "Please enter the ID of the product you want to buy (or 'done' to finish): ")
        if id_to_buy == "done":
            break

        for product in products:
            if int(id_to_buy) == product["id"]:
                count_to_buy = int(input(
                    "Please enter the quantity of the product you want to buy: "))

                if count_to_buy > product["count"]:
                    print(
                        f"Sorry, we don't have enough {product['name']} (ID: {product['id']})")
                    break
                else:
                    product["count"] = product["count"] - (count_to_buy)
                    item = {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "count": count_to_buy
                    }
                    cart.append(item)
                    break

        print("Your cart: ")
        for item in cart:
            print(
                f"{item['count']} of {item['name']} (ID: {item['id']}) --> Total cost for this product: {item['count'] * item['price']} Toman.")

    total_cost = 0
    for item in cart:
        total_cost = total_cost + (int(item["count"]) * int(item["price"]))
    print(f"The total cost of your purchase is {total_cost} Toman.")


def exit():
    pass


read_data()
show_menu()

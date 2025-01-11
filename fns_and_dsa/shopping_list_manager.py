def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        prompt = int(input("Enter a number: "))

        if prompt == 1:
            item = input("Add an item: ")
            shopping_list.append(item)

        elif prompt == 2:
            rm = input("Remove an item: ")
            if rm in shopping_list:
                shopping_list.remove(rm)
            else:
                print(f"{rm} not found in the shopping list.")

        elif prompt == 3:
            print("\nShopping List:")
            list(map(lambda value: print(value), shopping_list))

        elif prompt == 4:
            print("The program has ended.")
            break

        else:
            print("Invalid option. Please choose a valid option.")
        
        print()

main()

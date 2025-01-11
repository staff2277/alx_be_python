


def main ():
     shopping_list = []
     while True:
          print("Shopping List Manager")
          print("1. Add Item")
          print("2. Remove Item")
          print("3. View List")
          print("4. Exit")

          prompt = int(input("Enter a number: "))

          item = str(input("Add an item: ")) if prompt == 1 else None
          shopping_list.append(item) if prompt == 1 else None

          rm = str(input("Remove an item: ")) if prompt == 2 else None
          shopping_list.remove(rm) if prompt == 2 else None

          print() if prompt == 3 else None
          print("Shopping List") if prompt == 3 else None
          list(map(lambda value: print(value), shopping_list)) if prompt == 3 else None

          print()

          if prompt == 4:
               print("The program has ended")
               break

main()
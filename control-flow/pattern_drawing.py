size = int(input("Enter the size of the pattern: "))

i = size
count = 0

while i > 0:
    print("*", end="")
    i -= 1
    for _ in range(1):
        if count == size - 1:
            break
        elif i == 0:
            i = size
            count += 1
            print("\n")
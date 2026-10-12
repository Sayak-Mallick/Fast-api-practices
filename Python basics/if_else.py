num = input("Enter a number: ")

num = int(num)

if num % 2 == 0:
    print("Even")
    if num + 2 == 12:
        print("Great Job")
    else :
        print("Fine Job")
else:
    print("Odd")
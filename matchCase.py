# a = 4
#it supports on python version 10 onwards
a = int(input("Enter a Number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 12:
        print("Case is 12")
    case 41:
        print("Case is 41")
    case _:
        print("Case not found")

# Quick Quiz: Write a python program to print table of a number which lies between 1 to 10

while(True):

    table = int(input("Enter a number"))

    match table:
        case 1:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 2:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 3:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 4:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 5:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case _:
            print("Match not found. Please enter the number between 1 to 5")
            if table > 10:
                break
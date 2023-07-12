
try:
    #help = 10/0
    number = int(input("only numbers: ")); print(number)
except ZeroDivisionError as err: print(err)
except:
    print("invalid")
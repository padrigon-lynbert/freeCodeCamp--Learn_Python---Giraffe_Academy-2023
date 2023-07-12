def maxnum(num1, num2, num3):
    if num1 > num2 and num1 > num3: return print("num1: " + num1)
    elif num1 < num2 and num2 > num3: return print("num2: "+ num2)
    elif num1 < num3 and num1 < num3: return print("num3" + num3)
    if num1 == num2 and num1 == num3: return print("Equal value: " + num1)

num1 = input("n1: "); num2 = input("n2: "); num3 = input("n3: "); maxnum(num1, num2, num3)


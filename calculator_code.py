first = input( "enter first number :")
operator = input("+,-,*,%,/,// :")
second = input("enter second number :")
first= int(first)
second= int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "//":
    print(first // second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid operation")

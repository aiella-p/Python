operator = input("Enter an operator (+ - / *): ")
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

if operator == "+":
     result = num1 + num2
     print(num1 + num2)

elif operator == "-":
     result = num1 - num2
     print(round(num1 - num2))

elif operator == "*":
     result = num1 * num2
     print(round(num1 * num2))

elif operator == "/":
     result = num1 / num2
     print(round(num1 / num2))

else:
     print(f"{operator} is not valid")
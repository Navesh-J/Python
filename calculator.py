a=int(input("Enter 1st Number "))
b=int(input("Enter 2nd Number "))
operator=input("Enter an operator ")

match operator:
    case "+":print("Sum = ",a+b)
    case "-":print("Difference = ",a-b)
    case "*":print("Product = ",a*b)
    case "/":print("Division = ",a/b)
    case "//":print("Floor Division = ",a//b)
    case "%":print("Modulus = ",a%b)
    case "**":print("Exponent = ",a**b)
    case _:print("Invalid Operator")
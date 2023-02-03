import re

def calculator(num1, operator, num2):
    match operator:
        case "+": return num1 + num2
    match operator:
        case "-": return num1 - num2
    match operator:
        case "*": return num1 * num2
    match operator:
        # using pythons ternery operator in the return statement ( a if <cond> else b)
        case "/": return num1 / num2 if num2 != 0 else "Error, divided by 0!"

print("")
print("Better Calculator. Can use plus(+), minus(-), divide(/) or multiply(*) :-] ")
print("")

# saving the typed in calculation into a string, stripping white space
raw_input_string = input("Write a calculation in the form of \"2+2\" -> ".strip())

# extracting the operator and saving it in the operator variable
if "+" in raw_input_string:
    operator = "+"
if "-" in raw_input_string:
    operator = "-"
if "*" in raw_input_string:
    operator = "*"
if "/" in raw_input_string:
    operator = "/"
# using regular expression to split the two operands into a list [num1, num2]
input_string_list = re.split('[\+\-\*\/]', raw_input_string)

#casting the two (string) numbers into integers
floatnum1 = float(input_string_list[0])
floatnum2 = float(input_string_list[1])

result = calculator(floatnum1,operator,floatnum2)
print("")
print(f"{floatnum1} {operator} {floatnum2} = {result:.2f}")

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
print("Simple Calculator. capable of doing + - * / of SINGLE DIGIT numbers.. :-] ")
print("")

num1, operator, num2 = input("Write a calculation in the form of \"2+2\" -> ")
intnum1 = int(num1)
intnum2 = int(num2)

result = calculator(intnum1,operator,intnum2)
print("")
print(f"{intnum1} {operator} {intnum2} = {result}")

# calculator test cases
# print(calculator(1,"+",2))
# print(calculator(1,"-",2))
# print(calculator(1,"*",2))
# print(calculator(1,"/",2))
# print(calculator(1,"/",0))
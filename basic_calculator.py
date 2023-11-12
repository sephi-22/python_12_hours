def calculator (num1, num2, operation):
    match operation:
        case "add":
            return num1+num2
        case "subtract":
            return num1-num2
        case "divide":
            return num1/num2
        case "multiply":
            return num1*num2

input_str = input("Enter the first number, the second number, and the operation as Ex: (1,2,add): ")
x,y,o = map(str.strip, input_str.split(','))
print(calculator(int(x),int(y),o))
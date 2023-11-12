def convert_temperature(temp, direction):
    if direction == 'F_to_C':
        return (temp-32)*5/9
    elif direction == 'C_to_F':
        return (9/5)*temp+32
    else:
        raise ValueError("There was an Error!")

t = input("Enter the temperature value you want to convert:")
d = input("Enter the direction (F_to_C or C_to_F): ")
print(convert_temperature(float(t),d))


#This program reverses a string
def reverser (s):
    reversed_str=''
    for i in s:
        reversed_str = i + reversed_str
    return reversed_str

myString = input("Please Enter a string: ")
print("The reversed string is: " + reverser(myString))
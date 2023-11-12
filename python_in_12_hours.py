#Function to Summarize a Text File: Write a function that accepts a filename as a parameter,
# reads the file, and returns the number of lines, words, and characters in the file.
def summarize(i):
    i=i*2



#Check is string is palindrome
def is_palindrome(s):
    clean_str = s.replace(" ","").lower()
    if clean_str == clean_str[::-1]:
        print ("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

print("This is the palindrome checking function")
input_string = input("Please enter the string to check for palindrome")
is_palindrome(input_string)
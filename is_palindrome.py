#Function to check if given string is palindrome or not.
def is_palindrome(s):
    clean_str = s.replace(" ","").lower()
    if clean_str == clean_str[::-1]:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

#Test
my_str = input("Please enter a string to check if palindrome: ")
is_palindrome(my_str)

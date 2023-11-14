import re
#This is an email validator. Check if given string contains one '@' and at least one .
def is_valid_email(email):
    return '@' in email and '.' in email and email.count('@') == 1 and email[email.index('@')+1:].count('.')>=1

def is_valid_email_regex(email):
    return bool(re.match(r"^\w+@(\w+\.)?\w+\.\w+$", email,re.IGNORECASE))

myEmail = input("Enter your email address: ")
print(is_valid_email_regex(myEmail))
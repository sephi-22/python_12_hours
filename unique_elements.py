#Write a function that returns the unique elements in a list
def unique_elements(lst):
    return list(set(lst))

myList = [1,2,3,4,5,5,6,6,1,8,9,10]
print(unique_elements(myList))
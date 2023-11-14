#This is a frequency Counter that takes a list of numbers and returns a dictionary with keys being the numbers
#and values being the frequency of those numbers in the list.
def frequency_counter(numbers):
    frequency={}
    for x in numbers:
        frequency.update({x:numbers.count(x)})
    return frequency

myList = [1,4,3,5,6,7,2,2,4,5,2,3,6,7,8,4,6,7,5,2,3,4,5,6,7,8,5]
print(frequency_counter(myList))
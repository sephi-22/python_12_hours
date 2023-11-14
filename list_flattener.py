#This is a list flatterner
#Develop a function that takes a list of lists and flattens it to a single list without using any built-in Python flattening functions.
#Hint:Use a recursive function if a list is encountered.

def flatten_list(nested_list):
    flat_list=[]
    for x in nested_list:
        if isinstance (x,list):
            flat_list.extend(flatten_list(x))
        else:
            flat_list.append(x)
    return flat_list

list1 = [[1,2],[3,4],[[4,5],[4,5],[6,7]]]
print(flatten_list(list1))
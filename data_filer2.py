#Write a function that takes a list of dictionaries (representing people, with keys for name, age and profession)
#and a profession string, and returnas a new list with dictionaries where the profession matches the given string.

def filter_by_profession (people,profession):
    newlist=[]
    for x in people:
        for i in x:
            if x[i]==profession:
                newlist.append({i:x[i]})
    return newlist

dict1 = {
    "a":"Lawyer",
    "b":"Singer",
    "c":"Lawyer"
}
dict2 = {
    "d":"Lawyer",
    "e":"Lawyer",
    "f":"Lawyer"
}
dict3 = {
    "g":"Singer",
    "h":"Actor",
    "i":"Actor"
}
list1 = [dict1,dict2,dict3]
profession = 'Lawyer'
print(filter_by_profession(list1,profession))
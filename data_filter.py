#Write a function that takes a list of dictionaries (representing people, with keys for name, age and profession)
#and a profession string, and returnas a new list with dictionaries where the profession matches the given string.

def filter_by_profession (people,profession):
    return [person for person in people if person['profession'].lower()==profession.lower()]

people_list = [
    {'name':'Bob','profession':'Driver','age':60},
    {'name':'Casey','profession':'Skater','age':23},
    {'name':'Saul','profession':'Lawyer','age':40},
    {'name':'Jane','profession':'Lawyer','age':45},
    {'name':'Gordon','profession':'Chef','age':50},
    {'name':'Marco','profession':'Chef','age':60},
    {'name':'Janet','profession':'Singer','age':55},
    {'name':'Harvey','profession':'Lawyer','age':34},
    {'name':'Michael','profession':'Singer','age':25},
    {'name':'Matthew','profession':'Lawyer','age':30},
    {'name':'Josie','profession':'Singer','age':21}
    ]
profession = 'Lawyer'
print(filter_by_profession(people_list,profession))
#Write a function that merges two dictionaries. If there is a conflict between dictionaries (same key), the value
#from the second dictionary should be kept
def merge_dictionaries(dict1,dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dictx = {
    'Name':'Bob',
    'Age':30,
    'Address':'Los Angeles,California'
}
dicty = {
    'Age':32,
    'Job':'Web Developer'
}
print(merge_dictionaries(dictx,dicty))
#Create a function that counts how many times a word occurs in a sentence (passed as a string).
def word_occurence(sentence, word):
    return sentence.lower().split().count(word.lower())

print(word_occurence("This may be a secret surprise but I am a secret agent. Secret is surprising.","secret"))
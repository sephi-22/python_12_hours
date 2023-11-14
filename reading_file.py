#Program to read a file and summarize it. Count lines, words and characters.
def summarize_text_file(filename):
    with open(filename,'r') as file:
        content=file.read()
        print("The number of characters in the file is: "+ str(len(content)))
        content_words = content.split()
        print("The number of words in the file is: " + str(len(content_words)))
        content_lines = content.split('\n')
        print("The number of lines in the file is: " + str(len(content_lines)))


summarize_text_file('text_file.txt')
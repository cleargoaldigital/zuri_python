# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

'''
dictionary = {} #initialize an empty dictionary

file = open('story.txt', 'r') #open the text file in read mode.

read_data = file.read() #extract all the strings in the file. 

splitted_words = read_data.strip(' ,.\n?') #removes leading and trailing whitespaces and special characters in the strings.

new_text = splitted_words.split()
#loop through the splitted words and extract the frequency of unique words.
for word in new_text:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

print(dictionary) #print out the result.'''


# dictionary = {}
def read_file_content(filename):
    file = open(filename, "r")
    read_file = file.read()
    read_file = read_file.strip(' ,.\n?')
    
    return read_file

def count_words(text):
   dictionary = {}
   text = read_file_content("./story.txt")
   unique_words = text.split()
   for word in unique_words:
       if word not in dictionary:
          dictionary[word] = 1
       else:
          dictionary[word] += 1
   print(dictionary)

count_words("story.txt")

'''
{'Once': 1, 'upon': 1, 'a': 5, 'time': 1, 'psychology': 1, 'professor': 2, 'walked': 1, 'around': 1, 'on': 2, 'stage': 1, 'while': 1, 'teaching': 1, 'stress': 1, 'management': 1, 'principles': 1, 'to': 1, 'an': 1, 'auditorium': 1, 'filled': 1, 'with': 2, 'students.': 1, 'As': 1, 'she': 1, 'raised': 1, 'glass': 4, 'of': 2, 'water,': 1, 'everyone': 1, 'expected': 
1, 'they': 1, 'would': 1, 'be': 1, 'asked': 1, 'the': 2, 'typical': 1, 'half': 2, 'empty': 1, 'or': 1, 'full': 1, 'question.': 1, 'Instead,': 1, 'smile': 1, 'her': 1, 'face,': 1, 'asked,': 1, 'How': 1, 'heavy': 1, 'is': 1, 'this': 1, 'water': 1, 'I': 1, 'am': 1, 'holding': 1}
'''
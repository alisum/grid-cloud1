from collections import Counter

text = input()
# Cleaning text and lower casing all words
for char in '-.,\n':
    text=text.replace(char,' ')
text = text.lower()
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
word_list = text.split()
word_count = Counter(word_list).most_common()
print(sum(map(lambda x: x[1], word_count)))

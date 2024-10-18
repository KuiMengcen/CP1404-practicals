from operator import itemgetter

word_to_count = {}
word_count = 0
word_length = 0

text = input("Enter text: ").split()
text = sorted(text)

print(text)

for word in text:
    word_count = text.count(word)
    word_to_count[word] = word_count

print(word_to_count)
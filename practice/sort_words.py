
words = input()
new_words = ''
words = words.split(' ')

for word in words:
    sorted_string = ''.join(sorted(word.lower()))
    new_words += sorted_string + ' '

new_words.rstrip()
print(new_words)





s = input("Give me a string: ")

new_s = ""
words_list = s.split(' ')

for word in words_list:
    lowercase_word = word.lower()
    sorted_w = "".join(sorted(lowercase_word))
    new_s += sorted_w + ' '

new_s.rstrip()
print(new_s)

# OR

lowered_string = s.lower()

words = lowered_string.split()
sorted_word_list = ''

for word in words:
    sorted_word = sorted(word)
    sorted_word_list = "".join(sorted_word)

    print(f"{sorted_word_list}",end=' ')



s = input("Give me a string: ")

new_s = ""
words_list = s.split(' ')

for word in words_list:
    lowercase_word = word.lower()
    sorted_w = "".join(sorted(lowercase_word))
    new_s += sorted_w + ' '

new_s.rstrip()
print(new_s)


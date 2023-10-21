
words = input("Give a string - I'll change the order of words and the capitalization: ")
words = "Hello World"
words = words.split(' ')

new_words = []

for word in words:
    sorted_string = (sorted(word.lower()))
    new_words.append(sorted_string)

for word in new_words:
    print(word)

# ----------------
# Option 1
# ----------------

s = "Hello World"
new_words = ''
words_list = s.split(' ')

for word in words_list:
    lowercase_word = word.lower()
    sorted_word = ''.join(sorted(lowercase_word))
    new_words += sorted_word + ' '

new_words.rstrip()

print(new_words)

# ----------------
# Option 2
# ----------------
s = "Hello World"
new_s = ""

words_list = s.split(" ")

for word in words_list:
	new_s += "".join(sorted(word.lower())) + " "

new_s.rstrip()

print(new_s)
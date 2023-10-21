
words = input("Give a string - I'll change the order of words and the capitalization: ")

words = words.split(' ')
print(words)

reversed_words = []

for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word.swapcase())

result = ' '.join(reversed_words)
print(result)


#---------------------
s = "Hello World"

words_list = s.split(" ")
new_s = ""

for word in words_list:
	reversed_word = "".join(reversed(word))
	swapped_case = reversed_word.swapcase()
	new_s += swapped_case + " "

new_s.rstrip()

print(new_s)
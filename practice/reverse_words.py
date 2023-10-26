
words = input('Give me words: ')



words = words.split(' ')

for word in words:
    word = word[::-1].swapcase()
    print(word, end=' ')


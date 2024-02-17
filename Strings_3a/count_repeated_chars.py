s = input("Give me a string: ")

repeated_count = 0
repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_count += 1
		repeated_chars.append(char)

print(repeated_count)

if len(repeated_chars) > 0:
	for char in sorted(repeated_chars):
		print(char, end=" ")
else:
	print(None)

print()
# OR
	
s = input("Give me a string: ")
sorted_string = sorted(s)
# print(sorted_string)

letters = []


for char in sorted_string:
    if (s.count(char) > 1) and (char not in letters):
        letters.append(char)

print(len(letters))
if len(letters) == 0:
    print('None')
elif len(letters) == 1:
    print(f"\"{letters[0]}\"")
else:
    for char in letters:
        print(char, end=' ')
        

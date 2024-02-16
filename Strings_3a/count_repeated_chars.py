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
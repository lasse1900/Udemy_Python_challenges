
# s = input()
# s2 = s

# s2 = list('')
# bag = list('')
# print(s2)
# count = 0


# for i in range(len(s)):
#     if s[i] not in s2:
#         s2.append(s[i])
#         print('Yes')
#     else:
#         print('No')
#         count += 1
#         bag.append(s[i])

# print(s2)

# print(count)
# print(bag)


s = input()

repeated_count = 0
repeated_chars = []

for char in s:
    if (s.count(char) > 1 and char not in repeated_chars):
        repeated_count +=1
        repeated_chars.append(char)

sorted(repeated_chars)
print(repeated_count)

if repeated_count > 0:
    for i in range(repeated_count):
        print(repeated_chars[i],end=' ')
else:
	print(None)
	

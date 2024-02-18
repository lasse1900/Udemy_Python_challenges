# string_1 = input("Give first set: ")
# string_2 = input("Give second set: ")
# s1 = set(string_1)
# s2 = set(string_2)

s1 = {1,2,3,4,5,6}
s2 = {1,4,5}
intersection = set()

print(s1, s2)

if s1.isdisjoint(s2):
    print("{}")
else:
    intersection = set(sorted(s1 & s2))

    print(intersection)


# OR
intersection = set()

for elem in s1:
    if elem in s2:
        intersection.add(elem)

print(intersection)







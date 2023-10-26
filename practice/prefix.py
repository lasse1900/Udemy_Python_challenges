
s = input()
prefix = input()

if s[0:len(prefix)] == prefix:
    print(True)
else:
    print(False)

print(s[0:len(prefix)] == prefix)


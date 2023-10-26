
s = input()
suffix = input()

if s[len(s)-len(suffix):] == suffix:
    print(True)
else:
    print(False)
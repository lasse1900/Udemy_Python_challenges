
s = input()
ret = False

for i in range(len(s)):
    if s[i].isdigit():
        ret = True
    else:
        ret = False
        break

print(ret)
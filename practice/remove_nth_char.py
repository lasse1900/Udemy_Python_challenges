
s = input()
n = int(input())

if (n > len(s) or len(s) == 0):
    print(s)

else:
    for i in range(len(s)):
        if i != n:
            print(s[i], end='')
        else:
            continue
            


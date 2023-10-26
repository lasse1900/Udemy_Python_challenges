
import string

# s = "The quick brown fox jumps over the lazy dog"
s = "abcdefghijklmnopqrstuvwxyz"
s2 = ''
# for i in range(len(s)):
#     if s[i] != ' ':
#         s2 += s[i] 

s2 = s.replace(' ','')

set_s = set(s2.lower())
print(set_s == set(string.ascii_lowercase))
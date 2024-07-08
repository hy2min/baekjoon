
s = list(str(n))
leng = len(s)

i = leng - 2
while i >= 0 and s[i] >= s[i+1] :
    i -= 1

j = leng - 1
while s[j] <= s[i] :
    j -= 1
s[i], s[j] = s[j], s[i]

s = s[:i + 1] + sorted(s[i + 1:])

print(int(''.join(s))) 
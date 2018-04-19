s = input()
i = 0
j = 1
x = len(s)
while j <= x:
    n = 1
    while s[i] == s[j]:
        n += 1
        i += 1
        j += 1
    else:
        if j <= x:
            print(s[i], n)
            i += 1







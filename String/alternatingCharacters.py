def alternatingCharacters(s):
    counter = 0
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                counter = counter + 1
        except:
            pass
    return counter


print(alternatingCharacters("AAABBB"))

# SCORE = 100

def makeAnagram(a, b):

    if len(a) > len(b):
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    for char in greater:
        if char in smaller:
            smaller = smaller.replace(char, "", 1)
            greater = greater.replace(char, "", 1)
    return len(greater) + len(smaller)


print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))

# SCORE = 100

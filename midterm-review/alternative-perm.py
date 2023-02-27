letter = "a"
words = [ "bc", "cb" ]

def ben(letter, words):
    result = []
    for word in words:
        line = []
        for index in range(len(word)+1):
            line += [ word[0:index] + letter + word[index:] ]
        result += line
    return result

a = ben(letter, words)
print( a ) # [ "abc", "bac", "bca", "acb", "cab", "cba" ]

def perm(word):
    if len(word) <= 1:
        return [ word ]
    else:
        return ben(word[0], perm(word[1:]))

print(perm("hat"))
print(perm("race"))
print(len(perm("whatever")) == 40320)

assert sorted(perm("hat")) == sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']), "First assert fails."
assert len(perm("race")) == fact(len("race")), "Second assert fails."
assert len(perm("whatever")) == 40320, "Third assert failed."
print ("All assertions passed without a problem")

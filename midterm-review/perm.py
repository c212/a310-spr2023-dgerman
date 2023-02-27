def perm(word):
    answer = []
    if len(word) == 0:
        return [ "" ]
    for i in range(len(word)):
        letter = word[i]
        remaining = word[:i] + word[i+1:]
        print(letter + " followed by permutations of ('" + remaining + "')")
        a = perm(remaining)
        for w in a:
            answer = answer + [ letter + w ]
    return answer


def groupAnagrams(words):

    anagramsGroup = {}

    for word in words:
        sortedWord = "".join(sorted(word))

        if sortedWord in anagramsGroup:
            anagramsGroup[sortedWord].append(word)
        else:
            anagramsGroup[sortedWord] = [word]

    return list(anagramsGroup.values())


if __name__ == '__main__':

        s = ['awd','dwa','casa','asa','casada','asac']

        print(groupAnagrams(s))
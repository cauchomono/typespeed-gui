from typetest import TypeTest

with open("MostUsedWords.txt") as wordsTxt:
    word_list = wordsTxt.read().split("\n")



game = TypeTest(word_list)
#q1
def secretCode(string):
    newString = ""
    for i in string:
        newString = newString + str(ord(i)) + " "
    return newString

print(secretCode("cat"))

#q2
#Write a program similar to the morphology program for plurals discussed in class. Your program should take a single word as input, modifying it as appropriate, and adding ing to the end of the word. Specifically, given words in the Input column of the following table, it should return the corresponding Output word. The decisions about how to modify the words should be based on the final three letters of the input word. The status of these final 3 letters as vowels (a,e,i,o,u) or consonants (other letters) is important. In some cases, the final letter of the input word should be repeated before adding ing. In some cases, the final letter of the input word should be deleted before adding ing. Remember to use slices to represent parts of words. See slides for details about slices (using both positive and negative integers). Hint: to keep things simple, convert all input to lower case, using word = word.lower(), before running your code on that word.
#Please note that the "correct" answer should successfully convert the words in the input column to the words in the output column, while not referring to specific words, e.g., there should be no rules of the form "if word=='sit': return('sitting')". Instead the program should use rules referring to letters at the ends of words to predict the correct endings. These rules should apply to both words in the input list below and those not listed. However, your system will not be penalized for incorrectly assigning an -ing form for a word not listed below.
def addIng(word):
    if word[-3:] == "ing":
        return word
    elif word[-3:] == "eep":
        return word + "ing"



print(addIng("running"))
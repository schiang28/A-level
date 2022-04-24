# FIX THE ERRORS OR OMISSIONS
# WHEREVER YOU MAKE A CHANGE ADD A COMMENT SYNTAX/LOGIC/RUNTIME
# TO SHOW WHICH TYPE OF ERROR YOU HAVE IDENTIFIED/CORRECTED
# This program should input a sentence
# and output the number of vowels that it contains
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numVowels = 0
VOWELS = "aeiou"
# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
def countVowels(txt, vowel):
    count = 0
    for i in range(len(txt)):
        if txt[i] == vowel:
            count += 1
        return count


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
sentence = input("enter a sentence: ")
for v in VOWELS:
    numVowels += countVowels(sentence, v)

print(f"number of vowels is {numVowels}")
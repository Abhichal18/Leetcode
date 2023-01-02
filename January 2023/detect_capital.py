class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # store count of capital letters in word
        capital=0
        # iterating over word and incrementing capital if the character is in uppercase
        for i in word:
            if i.isupper():
                capital+=1
        # if word length is equal to capital count -> all letters are in uppercase -> True
        # if capital letters count is zero -> all letters are in lowercase -> True
        # if capital letters count is one and it's the first letter of word -> True
        # otherwise -> False
        if len(word)==capital or capital==0 or (capital==1 and word[0].isupper()):
            return True
        else:
            return False

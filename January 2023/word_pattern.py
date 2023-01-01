class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # dictionary to store the mapping
        d=dict()
        # converting s into list of words
        s=s.split()
        # checking if length of words in s is equal to characters in pattern
        # if not return False
        if len(s)==len(pattern):
            # iterate over pattern and s at the same time
            for i in range(len(s)):
                # if the character in pattern at ith position is available in
                # dictionary and the word at ith position in s is not similar
                # to the word corresponding to the character in the dictionary
                # then return False 
                if pattern[i] in d:
                    if d[pattern[i]]!=s[i]:
                        return False
                # otherwise set the word for the corresponding character in dictionary
                else:
                    d[pattern[i]]=s[i]
            # if total distinct characters in dictionary is not equal to the distinct
            # values in the dictionary then return False.
            # (This is to check if there is one to one mapping from s to pattern as well)
            if len(d)!=len(set(d.values())):
                return False
            return True
        else:
            return False

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # stores frequency of difficulty levels
        d=dict()
        for i in tasks:
            # if difficulty level already in dictionary increment it by 1
            # else create the difficulty level in dictionary and set it to 1
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # stores the min no of rounds to complete all the tasks
        min_rounds=0
        # iterating in dictionary
        for i in d:
            # if the frequency of difficulty level is 1
            # we can't complete the tasks. So, returning -1
            if d[i]==1:
                return -1
            else:
                # if frequency of difficulty level is divisible by 3
                # we are adding the quotient into min_rounds
                if d[i]%3==0:
                    min_rounds+=d[i]//3
                # if not disible by 3 we add (quotient+1) into min_rounds
                else:
                    min_rounds+=(d[i]//3)+1
        return min_rounds

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        # Split the individual words into a list
        words = sentence.split(' ')

        # If the sentence is 1 single word only the first and last characters must match
        if len(words) == 1:
            return True
        
        for i in range(len(words) - 1):
            # Compare the last character of the current word with the first character of the next word
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # All checks have passed, so the `sentence` is circular
        return True

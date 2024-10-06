class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Add the words from each sentence into a deque
        sentence1 = deque(sentence1.split(' '))
        sentence2 = deque(sentence2.split(' '))

        # Pop all of the matching prefixes
        while sentence1 and sentence2 and sentence1[0] == sentence2[0]:
            sentence1.popleft()
            sentence2.popleft()
        
        # Pop all of the matching suffixes
        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()
        
        # If either one of the deques was completely emptied, the sentences are "similar"
        return len(sentence1) == 0 or len(sentence2) == 0

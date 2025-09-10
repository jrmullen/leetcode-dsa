class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = defaultdict(int) # Count the number of occurrences of each character in magazine

        # If the ransomNote has more characters than the magazine exit immediately
        if len(ransomNote) > len(magazine):
            return False

        # Count each character in the magazine
        for char in magazine:
            freq[char] += 1
        
        for c in ransomNote:
            if c not in freq or freq[c] == 0: 
                return False
            
            freq[c] -= 1 if freq[c] > 0 else 0 # Decrement the character count
        
        return True

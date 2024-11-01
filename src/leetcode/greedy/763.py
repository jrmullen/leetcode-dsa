result = []
        partitionStart = 0
        partitionEnd = 0
        partitionSize = 0

        # Track the LAST index each character appears in `s`
        lastIndex = {char: i for i, char in enumerate(s) }

        for i, char in enumerate(s):
            partitionSize += 1 # Bump the partition length
            # Each time a new character is encountered in the partition we must re-evaluate the `partitionEnd` using its `lastIndex`
            partitionEnd = max(partitionEnd, lastIndex[char])
            
            # If the `partitionEnd` has been reached without encountering any new characters, it is a valid partition
            if i == partitionEnd:
                result.append(partitionSize) # Add the `partitionSize` to the `result` list
                partitionStart = i + 1 # Bump `partitionStart` so the next partition starts with the next character
                partitionSize = 0 # Reset the `partitionSize` count
        
        return result

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders alphabetically
        folder.sort()

        # Add the first folder to the result list
        result = [folder[0]]

        # Iterate over the sorted list of folders starting at the second element
        for i in range(1, len(folder)):
            # If the folder does not start with the folder previously added to the `result` list, it is not a sub-folder
            if not folder[i].startswith(result[-1] + '/'):
                result.append(folder[i])
        return result

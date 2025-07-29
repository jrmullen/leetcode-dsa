class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [] # Tuple (location, count)

        # Iterate over each trip in the list
        for count, src, dest in trips:
            locations.append((src, count)) # At the source location passengers get in the car
            locations.append((dest, -count)) # At the destination location passengers get out of the car
        
        locations.sort() # Sort the list of locations so they can be processed sequentially
        
        total = 0 # Track the total number of passengers in the car
        for location, passengers in locations:
            total += passengers # Update the total to reflect passengers getting in/out

            if total > capacity:
                return False # If the total number of passengers ever exceeds the allowed capacity, return False
        
        return True

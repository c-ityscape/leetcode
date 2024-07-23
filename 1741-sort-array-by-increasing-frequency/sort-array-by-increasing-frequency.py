from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count frequencies
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Step 2: Convert dictionary to a list of (number, frequency) tuples
        count_items = list(count.items())
        
        # Step 3: Sort the list of tuples
        # We will sort by frequency first (ascending) and by number second (descending)
        for i in range(len(count_items)):
            for j in range(i + 1, len(count_items)):
                # Compare frequencies
                if count_items[i][1] > count_items[j][1]:
                    # Swap if the frequency of i is greater than j
                    count_items[i], count_items[j] = count_items[j], count_items[i]
                elif count_items[i][1] == count_items[j][1]:
                    # If frequencies are the same, sort by number in descending order
                    if count_items[i][0] < count_items[j][0]:
                        # Swap if the number of i is smaller than j
                        count_items[i], count_items[j] = count_items[j], count_items[i]
        
        # Step 4: Build the result list
        res = []
        for num, freq in count_items:
            res.extend([num] * freq)
        
        return res

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map_val = {}
        
        for num in nums:
            original_num = num
            new_num = 0
            tens = 1
            
            if num == 0:
                new_num = mapping[0]
            else:
                while num > 0:
                    rem = num % 10
                    new_num = new_num + mapping[rem] * tens
                    num = num // 10
                    tens *= 10
                    
            map_val[original_num] = new_num
        
        # Sort based on the mapped values
        sorted_nums = sorted(nums, key=lambda x: map_val[x])
        
        return sorted_nums
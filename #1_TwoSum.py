class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define hashmap to store value and index pairs of inputted integers
        hashMap = {}
        
        # One pass search through integers
        for index, num in enumerate(nums):
            # Determine what is the complement of the current integer we are considering
            complement = target - num
            # Check if the compliment already exists in the hashmap, if it does return it and the current integer
            if complement in hashMap:
                return [hashMap[complement], index]
            
            # If we did not find the complement, add the current integer and its index to the hashmap
            hashMap[num] = index
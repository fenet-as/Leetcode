class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = []
        for i,v in enumerate(nums):
            numbers.append((v,i))
        numbers.sort(key = lambda x:x[0])


        i = 0
        j = len(numbers)-1
        while i < j:
            ie = numbers[i]
            je = numbers[j]
            sm = ie[0]+je[0] 
            if sm == target:
                return [ie[1],je[1]]   
            elif sm < target:
                i += 1
            elif sm > target:
                j -= 1
        
            

            

        
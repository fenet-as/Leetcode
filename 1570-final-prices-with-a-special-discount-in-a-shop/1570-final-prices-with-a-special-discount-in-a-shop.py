class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        [8,4,6,2,3]
        [3,2,6,4,8]

        '''

        res = [0]*len(prices)
        for i in range(len(prices)):
            ci = i+1
            while ci < len(prices) and prices[i] < prices[ci]:
                ci += 1
            if ci < len(prices):
                res[i] = prices[i] - prices[ci]
            else:
                res[i]= prices[i]
                
        return res
        

        

            


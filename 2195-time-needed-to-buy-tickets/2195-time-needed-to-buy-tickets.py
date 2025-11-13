class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        '''

        [2,3,2]

        '''
        ct = 0
        nf = True
        while nf:
            for i in range(len(tickets)):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    ct += 1
                if tickets[k] == 0:
                    return ct


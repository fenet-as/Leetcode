class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        resp_count = defaultdict(int)

        for day in responses:
            for response in set(day):
                resp_count[response] += 1
        

        most_frequent = [0,0]
        
        for e in resp_count:

            if resp_count[e] > most_frequent[1]:
                most_frequent[1] = resp_count[e]
                most_frequent[0] = e

            elif resp_count[e] == most_frequent[1]:
                if e < most_frequent[0]:
                    most_frequent[0] = e


        return most_frequent[0]


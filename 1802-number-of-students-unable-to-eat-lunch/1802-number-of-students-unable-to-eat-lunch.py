class Solution:
    def countStudents(self, students: List[int], sw: List[int]) -> int:
        '''
        reverse the sandw, i can use them as stack
        if elts match i pop both

        if the fron is the opp and the all elts in st are same i return 
        if sand are done also i return

        '''
        sw.reverse()
        std = deque(students)

        
        while std:
            e = std[0]
            if e  == sw[-1]:
                sw.pop()
                std.popleft()
            else:
                pe = std.popleft()
                std.append(pe)
            
            if len(set(std)) == 1 and len(sw) > 0:
                if std[0] != sw[-1]:
                    return len(std) 
                 
            if not sw:
                return len(std)

            # print(std)
            # print(sw)
        return 0

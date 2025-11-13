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

        ct1 = students.count(1)
        ct0 = students.count(0)
        
        while std:
            e = std[0]
            if e  == sw[-1]:
                sw.pop()
                pp = std.popleft()
                if pp == 1:
                    ct1 -= 1
                else:
                    ct0 -= 1
                
            else:
                pe = std.popleft()
                std.append(pe)
            
            if (ct1 == 0 or ct0 == 0) and len(sw) > 0:
                if std[0] != sw[-1]:
                    return len(std) 
                 
            if not sw:
                return len(std)

            # print(std)
            # print(sw)
        return 0

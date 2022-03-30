class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=''
        c=[]
        for i in range(len(digits)):
            b=b+str(digits[i])
        b=int(b)
        b=b+1
        b=str(b)
        for i in range(len(b)):
            c.append(int(b[i]))
        return c

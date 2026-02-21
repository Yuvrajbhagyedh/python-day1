class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if a>0 and b<0 or a<0 and b>0:
            flag=False
        elif a<0 and b<0:
            flag=True
            
        return flag    
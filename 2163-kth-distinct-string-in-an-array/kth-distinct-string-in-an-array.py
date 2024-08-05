class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count={}
        
        for i in arr:
            count[i]=1+count.get(i,0)
        r=0
        for key, value in count.items():
                if value==1:
                    r+=1
                if r==k:
                    return key
        return ""




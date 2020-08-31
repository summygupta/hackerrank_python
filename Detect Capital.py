class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        
        for i in range(0,len(word)):
            if word[i].isupper():
                count=count+1
        
        if not ( count==len(word) or( word[0].isupper() and count!=len(word) and count==1) or count==0):
            return False
        
        return True
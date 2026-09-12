class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sSort = sorted(s);
        # tSort = sorted(t);
        # if sSort == tSort:
        #     return True;
        # return False;
        sHM = {};
        tHM = {};

        for a in s:
            if sHM.get(a, 0)== 0:
                sHM[a] = 1;
            else:
                sHM[a]+=1;
        for b in t:
            if tHM.get(b, 0) == 0:
                tHM[b] = 1;
            else:
                tHM[b]+=1;
        if sHM == tHM:
            return True;
        return False;
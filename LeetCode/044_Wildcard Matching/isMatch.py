class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen,plen = len(s),len(p)
        snext,pnext = None,None
        si = pi = 0
        while si < slen:
            if pi < plen and (p[pi] == '?' or s[si] == p[pi]):
                si+=1
                pi+=1
            elif pi < plen and p[pi] == '*':
                snext = si+1
                pnext = pi
                pi+=1
            elif pnext != None:
                si = snext
                pi = pnext
            else :
                return False
        
        return p[pi:].count('*') == plen - pi
        
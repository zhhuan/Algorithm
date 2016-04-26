/*Determine whether an integer is a palindrome. Do this without extra space.
*@author Zhong Huan 
*@data 2016/4/26 
*
*/
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || x!=0 && x%10 == 0) return false;
        int tem = x,r = 0;
        while(tem){
            r = r * 10 + tem % 10;
            tem = tem / 10;
        }
        if(r == x)
            return true;
        return false;
    }
};
/*
@author  gaurav5
a more efficent way

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0|| (x!=0 &&x%10==0)) return false;
        int sum=0;
        while(x>sum)
        {
            sum = sum*10+x%10;
            x = x/10;
        }
        return (x==sum)||(x==sum/10);
    }
};
*/
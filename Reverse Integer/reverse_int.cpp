class Solution {
public:
    int reverse(int x) {
        long value = 0;
        while (x!=0){
            value =value*10+x%10;
            x = x/10;
        }
        if (value > 0)
            return value > INT_MAX ? 0:value;
        else 
            return value < INT_MIN ? 0:value;
    }
};
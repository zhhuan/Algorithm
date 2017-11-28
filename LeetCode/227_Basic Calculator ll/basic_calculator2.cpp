class Solution {
public:
    int calculate(string s) {
        istringstream str('+' + s + '+');
	    int total = 0, temp = 0, n;
		char op;
		while(str >> op){
			if(op == '+' or op == '-' ){
				total += temp;
				str >> temp;
				temp *= 44 - op;//op == '+' ? 1:-1;
			}
			else{
				str >> n;
				if(op == '*')
					temp *= n;
				else
					temp /= n;
			}
		}
		return total;
    }
};
/*
*Given an array of integers, return indices of the two numbers such that they add up to a specific target.
*You may assume that each input would have exactly one solution.
*Example:
*	Given nums = [2, 7, 11, 15], target = 9,
*	Because nums[0] + nums[1] = 2 + 7 = 9,
*return [0, 1].
*/
//author:ZhongHuan
//create date:2016/4/18
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		//Key is the number and value is its index in the vertor
		unordered_map<int,int> hash;
		vector<int> result;
		for(int i = 0; i < nums.size();i++){
			int numTofind = target - nums[i];
			//if numTofind is found in map,return result 	
			if(hash.find(numTofind)!=hash.end()){
				result.push_back(hash[numTofind]);
				result.push_back(i);
				return result;
			}
			
			//number was not found , put it in the map
			hash[nums[i]] = i;
		}
		return result;
    }
};
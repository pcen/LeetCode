#include <vector>
using namespace std;

class Solution
{
public:
	int searchInsert(vector<int>& nums, int target)
	{
		int index = -1;
		for (int i = 0; i < nums.size(); i++) {
			if (nums.at(i) == target || nums.at(i) > target && index == -1)
				index = i;
		}

		/* target is largest element when inserted */
		if (index == -1)
			index = nums.size();

		return index;
	}

};

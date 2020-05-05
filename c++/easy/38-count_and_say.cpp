#include <iostream>
#include <string>
using namespace std;

class Solution
{
	string stringify(string s) {
		string ret;
		int count = 0;
		char current = s.at(0);
		for (int i = 0; i < s.size(); i++) {
			if (s.at(i) == current) {
				count++;
			}
			else {
				ret.append(to_string(count));
				ret.push_back(current);
				count = 1;
				current = s.at(i);
			}
		}
		ret.append(to_string(count));
		ret.push_back(current);
		return ret;
	}

public:
	string countAndSay(int n)
	{
		if (n == 1)
			return "1";

		return stringify(countAndSay(n - 1));
	}

};

int main(void)
{
	auto sln = Solution();
	int param = 0;
	while (cin >> param) {
		cerr << sln.countAndSay(param) << "\n";
	}
	return 0;
}

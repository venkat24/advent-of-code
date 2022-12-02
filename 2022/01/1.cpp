#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	vector<int> cals;

	string current;
	int sum = 0;
	while (std::getline(std::cin, current)) {
		if (current.size() > 0) {
			int val = stoi(current);
			sum += val;
		}
		else {
			cals.push_back(sum);
			cout << "CURRENT:" << sum << endl;
			sum = 0;
		}
	}

	cals.push_back(sum);

	priority_queue<int> k;
	for (auto cal : cals) {
		k.push(cal);
	}

	int ans = 0;
	ans += k.top();
	k.pop();
	ans += k.top();
	k.pop();
	ans += k.top();
	k.pop();
	
	cout << ans << endl;
	return 0;
}

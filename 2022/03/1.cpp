#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int getPriority(char c) {
	if (isupper(c)) {
		return ((int)c - 64) + 26;
	}
	else {
		return ((int)c - 96);
	}

	return 0;
}

int main() {
	unordered_set<char> set;

	string line;
	int ans = 0;
	while (std::getline(std::cin, line)) {
		for (int i = 0; i < line.size() / 2; ++i) {
			set.insert(line[i]);
		}

		for (int i = line.size() / 2; i < line.size(); ++i) {
			if (set.find(line[i]) != set.end()) {
				cout << line[i] << " is a dupe!" << endl;
				ans += getPriority(line[i]);
				break;
			}
		}

		set.clear();
	}
	
	cout << ans << endl;
	return 0;
}

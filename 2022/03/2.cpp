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
	unordered_map<char, int> s;

	string line1;
	string line2;
	string line3;
	int ans = 0;
	while (std::getline(std::cin, line1) && std::getline(std::cin, line2) && std::getline(std::cin, line3)) {
		set<char> curr;
		for (int i = 0; i < line1.size(); ++i) {
			if (curr.find(line1[i]) == curr.end()) {
				s[line1[i]]++;
				curr.insert(line1[i]);
			}
		}
		curr.clear();

		for (int i = 0; i < line2.size(); ++i) {
			if (curr.find(line2[i]) == curr.end()) {
				s[line2[i]]++;
				curr.insert(line2[i]);
			}
		}
		curr.clear();

		for (int i = 0; i < line3.size(); ++i) {
			if (curr.find(line3[i]) == curr.end()) {
				s[line3[i]]++;
				curr.insert(line3[i]);
			}
			if (s[line3[i]] == 3) {
				cout << "Found ans " << line3[i] << endl;
				ans += getPriority(line3[i]);
				break;
			}
		}
		curr.clear();
		s.clear();
	}
	
	cout << ans << endl;
	return 0;
}

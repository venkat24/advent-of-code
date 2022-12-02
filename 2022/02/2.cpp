#include <iostream>
#include <bits/stdc++.h>
using namespace std;

char getAction(char theirs, char result) {
	if (result == 'D') return theirs;
	switch (result) {
		case 'W':
			switch (theirs) {
				case 'P': return 'S';
				case 'S': return 'R';
				case 'R': return 'P';
			}
		case 'L':
			switch (theirs) {
				case 'P': return 'R';
				case 'S': return 'P';
				case 'R': return 'S';
			}
	}

	return theirs;
}

int main() {
	vector<pair<char, char>> rounds;

	string line;
	while (std::getline(std::cin, line)) {
		pair<char, char> current;
		switch (line[0]) {
			case 'A': current.first = 'R'; break;
			case 'B': current.first = 'P'; break;
			case 'C': current.first = 'S'; break;
		}
		switch (line[2]) {
			case 'X': current.second = 'L'; break;
			case 'Y': current.second = 'D'; break;
			case 'Z': current.second = 'W'; break;
		}

		rounds.push_back(current);
	}

	int ans = 0;
	for (auto& [theirs, result] : rounds) {
		int score = 0;

		char mine = getAction(theirs, result);
		switch (mine) {
			case 'R': score += 1; break;
			case 'P': score += 2; break;
			case 'S': score += 3; break;
		}
		switch (result) {
			case 'W': score += 6; break;
			case 'D': score += 3; break;
		}

		cout << "They play " << theirs << " and I want " << result << ", so I play " << mine << endl;
		ans += score;
	}
	
	cout << ans << endl;
	return 0;
}

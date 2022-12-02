#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int getScore(char theirs, char mine) {
	if (theirs == mine) return 3;
	switch (theirs) {
		case 'R':
			switch (mine) {
				case 'P': return 6;
				case 'S': return 0;
			}
		case 'P':
			switch (mine) {
				case 'S': return 6;
				case 'R': return 0;
			}
		case 'S':
			switch (mine) {
				case 'R': return 6;
				case 'P': return 0;
			}
	}

	return 0;
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
			case 'X': current.second = 'R'; break;
			case 'Y': current.second = 'P'; break;
			case 'Z': current.second = 'S'; break;
		}

		rounds.push_back(current);
	}

	int ans = 0;
	for (auto& [theirs, mine] : rounds) {
		int score = 0;

		switch (mine) {
			case 'R': score += 1; break;
			case 'P': score += 2; break;
			case 'S': score += 3; break;
		}

		score += getScore(theirs, mine);
		ans += score;
	}
	
	cout << ans << endl;
	return 0;
}

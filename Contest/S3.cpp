#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <iomanip>  
#include <cmath>
#include <algorithm>
#include <unordered_map>

using namespace std; 

struct person {
	int p = 0;
	int w = 0;
	int d = 0;
	person(int p, int w, int d) {
		this->p = p;
		this->w = w;
		this->d = d;
	}
};

vector<person> persons;

long long getMinSum(int pos) { // input is the position of the concert
	long long sum = 0;
	for (const auto& p : persons) {
		// Calculate the minimum time to get to the concert for this person
		long long dist = abs(pos - p.p) - p.d;
		dist = max(0LL, dist);

		long long time = p.w * dist;
		sum += time;
	}
	return sum;
}

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		persons.push_back(person(a, b, c));
	}

	// binary search
	long long L = 0, R = 1e9;
	long long best = 0;
	while (L < R) {
		long long mid = (L + R) / 2;
		long long cur, next;
		cur = getMinSum(mid);
		next = getMinSum(mid + 1);
		if (cur > next) {
			L = mid + 1;
		}
		else {
			R = mid;
		}

	}
	best = getMinSum(L);
	cout << best;
}

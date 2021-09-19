// 소수 찾기

#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;

vector<int> v;
bool allUsed(int i, string numbers);

int solution(string numbers) {
    int answer = 0;
    int max = 0;

    for (int i = 0; i < numbers.size(); i++) {
        v.push_back(stoi(numbers[i]));    // numbers[i] 도 되나?
    }

    sort(v.begin(), v.end(), greater<int>());

    for (int i = 0; i < v.size(); i++) {
        max = max + (v[i] * pow(10, v.size() - 1 - i));
    }

    vector<bool> isPrime(max + 1, true);

    for (int i = 2; i <= max; i++) {
        if (isPrime[i]) {
            if (allUsed(i, numbers)) {
                answer++;
            }

            for (int j = 2; i * j <= max; j++) {
                isPrime[i * j] = false;
            }
        }
    }

    return answer;
}

bool allUsed(int i, string numbers) {
    string s = to_string(i);
    vector<bool> visit(v.size(), false);

    for (int j = 0; j < s.size(); j++) {
        int index = numbers.find(s.substr(j, 1));

        if (index >= numbers.size()) {
            return false;
        }
        else {
            numbers = numbers.substr(0, index) + numbers.substr(index + 1);
        }
    }

    return true;
}
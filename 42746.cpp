// 가장 큰 수

#include <string>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool cmp(string a, string b) {
    return (a + b > b + a);
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> sub;

    for (int i = 0; i < numbers.size(); i++) {
        sub.push_back(to_string(numbers[i]));
    }
    sort(sub.begin(), sub.end(), cmp);
    if (sub.at(0) == "0") {
        answer += "0";
        return answer;
    } else {
        for (int i = 0; i < sub.size(); i++) {
            answer += sub[i];
        }
    }

    return answer;
}
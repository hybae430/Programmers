// 주식가격

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;

    for (int i = 0; i < prices.size(); i++) {
        int tmp = prices[i];
        int idx = i;

        while (idx < prices.size()) {
            if (idx == (prices.size() - 1)) {
                break;
            }
            if (prices[idx] < tmp) {
                break;
            } else { idx++; }
        }

        answer.push_back(idx - i);
    }
    return answer;
}
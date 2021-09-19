// 프린터

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    queue<pair<int, int> > qu;
    priority_queue<int> pri;        // 비교용

    for (int i = 0; i < priorities.size(); i++) {
        qu.push({i, priorities[i]});
        pri.push(priorities[i]);
    }

    while (!qu.empty()) {
        if (qu.front().second == pri.top()) {
            if (qu.front().first == location) {
                return answer + 1;
            } else {
                answer++;
                qu.pop();
                pri.pop();
            }
        } else {
            qu.push(qu.front());
            qu.pop();
        }
    }

    return answer;
}
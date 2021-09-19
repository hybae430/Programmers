// 체육복

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;

    int status[n];

    for (int i = 0; i < n; i++) {
        status[i] = 0;
    }
    for (int i = 0; i < lost.size(); i++) {
        status[lost[i] - 1] -= 1;
    }
    for (int i = 0; i < reserve.size(); i++) {
        status[reserve[i] - 1] += 1;
    }

    for (int i = 0; i < n; i++) {
        if (status[i] == 1) {
            if (i - 1 >= 0) {
                if (status[i - 1] == -1) {
                    status[i - 1]++;
                    status[i]--;
                }
            }
        }
        if (status[i] == 1) {
            if (i + 1 < n) {
                if (status[i + 1] == -1) {
                    status[i + 1]++;
                    status[i]--;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (status[i] != -1) {
            answer++;
        }
    }

    return answer;
}
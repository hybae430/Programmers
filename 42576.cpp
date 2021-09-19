// 완주하지 못한 선수

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string answer = "";
    bool found = false;

    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());     // 참가자와 완주자 명단 정렬

    for (int i = 0; i < participant.size(); i++){
        if ((i <= completion.size()) && (completion[i] != participant[i])){
            answer += participant[i];
            found = true;
        }
        else if (i > completion.size()){
            answer += participant[i];
            found = true;
        }
        if (found) { break; }
    }

    return answer;
}
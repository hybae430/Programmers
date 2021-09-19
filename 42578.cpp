// 위장

#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    map<string, int> strM;

    for (int i = 0; i < clothes.size(); i++) {
        strM[clothes[i][1]]++;
    }
    int answer = 1;
    map<string, int>::iterator hash;
    for (hash = strM.begin(); hash != strM.end(); hash++) {
        answer *= hash -> second + 1;
    }

    return answer - 1;
}
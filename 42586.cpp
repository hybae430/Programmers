// 기능개발

// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
// 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> d;

    for (int i = 0; i < progresses.size(); i++) {
        int day = 0;
        int sum = progresses[i];
        while (sum + speeds[i] < 100) {
            sum += speeds[i];
            day++;
        }
        d.push_back(day + 1);
    }

    int max = 0;
    int com = 0;
    for (int i = 0; i < d.size(); i++){
        if (max < d[i]){
            if (com != 0){
                answer.push_back(com);
            }
            com = 1;
            max = d[i];
        } else {
            com++;
        }
    }
    answer.push_back(com);

    return answer;
}
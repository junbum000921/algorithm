#include <iostream>
using namespace std;

int main() {
    long long x, y;
    cin >> x >> y;

    int current_rate = (y * 100) / x; // 현재 승률 (정수 부분만)
    if (current_rate >= 99) { // 승률이 99% 이상이면 더 이상 변하지 않음
        cout << -1 << endl;
        return 0;
    }

    long long left = 1, right = 1e9; // 이분 탐색 범위
    long long result = -1;

    while (left <= right) {
        long long mid = (left + right) / 2;
        int new_rate = ((y + mid) * 100) / (x + mid); // 새로운 승률 계산

        if (new_rate > current_rate) {
            result = mid; // 조건을 만족하는 최소 게임 수 저장
            right = mid - 1; // 더 작은 값 탐색
        } else {
            left = mid + 1; // 더 큰 값 탐색
        }
    }

    cout << result << endl; // 결과 출력
    return 0;
}
#문제
'''
JOI는 친구 1부터 친구 N까지 총 N 명의 친구와 함께, 크리스마스 파티에 갔습니다. 크리스마스 파티 분위기도 달아오르니, JOI는 친구들과 함께 다음과 같은 게임을 하기로 했습니다.

가장 먼저, JOI는 N명의 친구 중 한 명을 선택합니다. 이제 그 친구를 '타겟'이라고 부릅시다.
JOI는 타겟으로 고른 친구에게, 타겟이 되었다는 것을 몰래 알려줍니다. 타겟이 아닌 친구들은 누가 타겟인지 알 수 없습니다.
타겟이 아닌 친구들은 각자 타겟이 누구일까 생각해서, 그 사람의 이름을 종이에 씁니다. 타겟은 자기자신의 이름을 종이에 씁니다.
모든 사람이 종이에 이름을 썼다면, JOI는 타겟의 이름을 발표합니다.
예상이 맞은 사람은 1점을 얻습니다. 당연히, 타겟은 자신의 이름을 적었으므로, 반드시 1점을 얻습니다. 예상이 빗나간 사람은 점수를 주지 않습니다.
추가로, 예상이 빗나간 사람의 수가 X명일 경우, 타겟은 추가로 X점을 얻습니다.
 JOI와 친구들은 이 게임을 M번 했습니다. M번의 게임을 했을 때, 각 친구들의 합계 점수를 구하세요.
'''
turn = int(input())
friend_number = int(input())
target = list(map(int, input().split()))

for i in range(0, turn + 1):
    a = list(map(int, input(). split()))
    for j in range(0, friend_number + 1):
        if target[i] == a[j]:




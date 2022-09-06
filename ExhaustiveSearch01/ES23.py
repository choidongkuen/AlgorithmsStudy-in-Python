# 날짜 : 2022 / 09 / 06
# 문제 : 겹치지 않은 선분 2
# 문제 설명 :
# N개의 선분이 주어졌을 때, 다른 선분과 전혀 겹치지 않는 선분의 수를 출력하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에 정수 N이 주어집니다.
# 그 다음 줄부터는 N개의 줄에 걸쳐 각 줄마다 x1과 x2가 공백을 사이에 두고 주어집니다. 이는 해당 선분의 끝점이 (x1, 0), (x2, 1)임을 의미합니다.
# 입력으로 주어지는 x1끼리는 겹쳐져 주어지지 않으며, x2끼리도 겹쳐져 주어지지 않음을 가정해도 좋습니다.
# 1 ≤ N ≤ 100
# -1,000,000 ≤ 주어지는 x의 값 ≤ 1,000,000

# 입력 예시 :
# 4
# -3 4
# 7 8
# 10 16
# 3 9

# 출력 예시 :
# 2


n = int(input()) # n개의 선분
arr = [tuple(map(int,input().split())) for _ in range(n)] # n개의 선분 정보
ans = 0 # 겹치지 않은 선분의 수

for i in range(n): # i 선분
    isOverlap = False # 하나라도 겹치면 true
    for j in range(n): # j 선분

        if( i == j ):continue

        x1 = arr[i][0]
        x2 = arr[i][1]

        x3 = arr[j][0]
        x4 = arr[j][1]

        if((x1 <= x3 and x2 >= x4) or (x1 >= x3 and x2 <= x4)):
            isOverlap = True
            break # j 가 속한 반복문 종료

    if(isOverlap is False):
        ans += 1

print(ans)
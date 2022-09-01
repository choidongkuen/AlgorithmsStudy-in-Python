# 날짜 : 2022/09/01
# 문제 : 겹치지 않은 사각형의 넓이

# 문제 설명 : 좌표평면위에 직사각형 A, B를 먼저 붙이고 그 위에 직사각형 M을 붙였습니다.
# 아직 남아있는 (M으로 덮이지 못한) 직사각형 A, B의 넓이의 합을 구하는 프로그램을 작성해보세요.
# 단, 직사각형 A, B는 겹치지 않게 주어진다고 가정해도 좋습니다.

# 입력 형식 : 첫 번째 줄에는 직사각형 A의 좌측 최하단의 좌표(x1, y1)와 우측 최상단의 좌표(x2, y2)가 공백을 사이에 두고 주어집니다.
# 두 번째 줄에는 직사각형 B의 좌측 최하단의 좌표(x1, y1)와 우측 최상단의 좌표(x2, y2)가 공백을 사이에 두고 주어집니다.
# 세 번째 줄에는 직사각형 M의 좌측 최하단의 좌표(x1, y1)와 우측 최상단의 좌표(x2, y2)가 공백을 사이에 두고 주어집니다.
# -1,000 ≤ x1 < x2 ≤ 1,000
# -1,000 ≤ y1 < y2 ≤ 1,000

# 입력 예시 :
# 1 2 3 5
# 6 0 10 4
# 2 1 8 3

# 출력 예시 :
# 17

OFFSET = 1000
MAX_N = 2000
arr = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]  # 2차원 배열 선언

for i in range(1, 4):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for row in range(x1, x2):
        for col in range(y1, y2):
            arr[row][col] = i

ans = 0
for i in range(MAX_N + 1):
    for j in range(MAX_N + 1):
        if (arr[i][j] == 1 or arr[i][j] == 2):
            ans += 1

print(ans)


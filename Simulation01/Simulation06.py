# 날짜 : 2022/09/01
# 문제 : 색종이의 총 넓이
# 문제 설명 : 좌표평면위에 가로세로 길이가 8이고 넓이가 64인 색종이가 N장 주어집니다.
# 이 N장 색종이의 각 좌측하단의 꼭지점이 주어졌을 때 모든 색종이가 붙여진 이후의 총 넓이를 구하는 프로그램을 작성해보세요.
# 단, 모든 색종이는 좌표평면위에서 (-100, -100)을 좌측하단으로 (100, 100)을 우측상단으로 하는 정사각형 범위를 벗어나지 않는다고 가정해도 좋습니다.
# 또한 겹치는 영역은 단 한번만 넓이에 포함시킵니다.

# 입력 형식 : 첫 번째 줄에는 정수 N이 주어집니다.
# 두 번째 줄부터 각 줄마다 정사각형 크기인 색종이의 좌측하단 꼭지점의 위치가 총 N번 주어집니다.
# 1 ≤ N ≤ 100

# 입력 예시 :
# 3
# 0 0
# 4 0
# 0 4

# 출력 예시 :
# 128

OFFSET = 100
MAX = 200

arr = [[0 for _ in range(MAX + 1)] for _ in range(MAX + 1)]
n = int(input())

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    x, y = x + OFFSET, y + OFFSET

    for row in range(x, x + 8):
        for col in range(y, y + 8):
            if arr[row][col] == 0:
                arr[row][col] = 1

cnt = 0
for row in range(MAX + 1):
    for col in range(MAX + 1):
        if arr[row][col] == 1:
            cnt += 1

print(cnt)




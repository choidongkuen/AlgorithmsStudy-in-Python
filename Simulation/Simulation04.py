# 날짜 : 2022/09/01
# 문제 : 사각형 칠하기
# 문제 설명 : 2차 평면 위에 N개의 직사각형이 주어집니다. 이 직사각형들이 만들어내는 총 넓이를 구하는 프로그램을 작성해보세요.

# 입력 형식 : 첫 번째 줄에 N이 주어집니다.
# 두 번째 줄부터는 N개의 줄에 걸쳐 각 줄마다 x1, y1, x2, y2 값이 공백을 사이에 두고 주어집니다.
# 이는 (x1, y1), (x2, y2)를 양 끝으로 직사각형임을 의미합니다.
# 1 ≤ N ≤ 10
# -100 ≤ x1 < x2 ≤ 100

# 입력 예시
# 2
# 0 1 4 5
# 2 2 6 4

# 출력 예시
# 20

OFFSET = 100
MAX_N = 200

arr =[
    [0] * (MAX_N +1)
    for _ in range(MAX_N + 1)
]

n = int(input())

for i in range(n):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(x1 , x2):
        for col in range(y1, y2):
            arr[row][col] += 1

s = 0
for i in range(MAX_N + 1):
    for j in range(MAX_N + 1):
        if(arr[i][j] != 0):
            s += 1
print(s)
# 날짜 : 2022/09/06
# 문제 : 좌표평면 위의 특정 구역2
# 문제 설명 :
# 좌표평면 위에 점 N개가 있습니다. 그 N개의 점들 중 정확히 하나의 점만 빼서,
# 뺀 후의 모든 점들을 포함하는 직사각형의 넓이를 최소로 하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에 정수 N이 주어집니다.
# 그 다음 줄부터는 N개의 줄에 걸쳐 한 줄에 하나씩 각 점의 위치 (x, y)가 공백을 사이에 두고 주어집니다.
# 3 ≤ N ≤ 100
# 1 ≤ x, y ≤ 40,000

# 입력 예시 :
# 4
# 2 4
# 1 1
# 5 2
# 17 25

# 출력 예시 :
# 12

import sys

maxVal = sys.maxsize # 정수의 최대값
n = int(input()) # n개의 점
arr = [tuple(map(int,input().split())) for _ in range(n)] # n개의 점 입력

ans = maxVal # 모든 점을 포함하는 최소 너비

for i in range(n):
    maxRow,minRow,maxCol,minCol = 0,maxVal,0,maxVal

    for j in range(n):
        if i == j: continue

        maxRow = max(maxRow, arr[j][0])
        minRow = min(minRow, arr[j][0])
        maxCol = max(maxCol, arr[j][1])
        minCol = min(minCol, arr[j][1])
        # 각각 업데이트

    area = (maxCol - minCol) * (maxRow - minRow)

    ans = min(ans,area)

print(ans)

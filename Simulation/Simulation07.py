# 날짜 : 2022/09/02
# 문제 : 잔해물을 덮기 위한 사각형의 최소 넓이

# 문제 설명 : 첫 번째 직사각형이 먼저 놓여 있고, 두 번째 직사각형이 그 다음 놓아졌을 때
# 그 이후에 남아있는 첫 번째 직사각형의 잔해물을 덮기 위한 최소 직사각형의 넓이를 구하는 프로그램을 작성해보세요.

# 입력 형식 : 첫 번째 줄에 첫 번째 직사각형에 해당하는 좌측하단의 좌표와 우측상단의 좌표 (x1, y1), (x2, y2)가 공백을 사이에 두고 주어집니다.
# 두 번째 줄에 두 번째 직사각형에 해당하는 좌측하단의 좌표와 우측상단의 좌표 (x1, y1), (x2, y2)가 공백을 사이에 두고 주어집니다.
# -1,000 ≤ x1 < x2 ≤ 1,000
# -1,000 ≤ y1 < y2 ≤ 1,000

# 입력 예시 :
# 2 1 7 4
# 5 -1 10 3


# 출력 형식 :
# 15

OFFSET = 1000
MAX = 2000

arr = [[0 for _ in range(MAX+1)] for _ in range(MAX+1)]
for i in range(1,3):
    x1,y1,x2,y2 = tuple(map(int,input().split()))
    x1,x2 = x1+OFFSET,x2+OFFSET
    y1,y2 = y1+OFFSET,y2+OFFSET
    for row in range(x1,x2):
        for col in range(y1,y2):
            arr[row][col] = i

# 첫번째 사각형은 1로 두번째 사각형은 2로 채움
# 가려지지 않는 부분을 둘러싸는 사각형의 최소 넓이를 구하기 위해서는 (최대 행 - 최소 행) * (최대 열 - 최소 열) > 1로 채워져 있는 칸
max_row,min_row,max_col,min_col = 0,MAX,0,MAX
is_pos = False

for row in range(MAX+1):
    for col in range(MAX+1):
        if arr[row][col] == 1:
            max_row = max(row,max_row)
            max_col = max(col,max_col)
            min_row = min(row,min_row)
            min_col = min(col,min_col)
            is_pos = True

if not is_pos:
    result = 0
else:
    result = (max_row - min_row+1) * (max_col - min_col+1)
print(result)
# 날짜 : 2022/09/07
# 문제 : 행복 수열의 개수
# 문제 설명 :
# 1이상 100이하의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.
# 이때 행복한 수열이라는 것은 다음과 같이 정의됩니다.
# 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여
# 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해보세요.
# 예를 들어, 다음과 같은 경우라면, 첫 번째 행을 골랐을 경우와 첫 번째 열을 골랐을 경우에만 행복한 수열이 되므로, 총 행복한 수열의 수는 2개가 됩니다.

# 입력 형식 :
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 연속해야 하는 숫자의 수를 나타내는 m이 공백을 사이에 두고 주어집니다.
# 두 번째 줄부터는 n개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며,
# 이 정보는 1이상 100이하의 숫자가 각각 공백을 사이에 두고 주어집니다.
# 1 ≤ m ≤ n ≤ 100

# 입력 예시 :
# 3 2
# 1 2 2
# 1 3 4
# 1 2 3

# 출력 예시 :
# 2


n, m = tuple(map(int, input().split()))  # 격자 크기 입력
grid = [list(map(int, input().split())) for _ in range(n)]  # 격자 입력
seq = [0] * n  # 특정 순간의 원소들을 담기 위한 1차원 배열

numOfhappyseq = 0  # 행복 수열 갯수


def isHappy():
    consecutive, maxConsecutive = 1, 1
    for i in range(1, n):
        if (seq[i] == seq[i - 1]):
            consecutive += 1
        else:
            consecutive = 1

        maxConsecutive = max(maxConsecutive, consecutive)  # 특정 테스트 중인 수열의 최대 동일 원소 연속 횟수 업데이트

    return maxConsecutive >= m


for i in range(n):  # 각 행
    for j in range(n):  # 각 열
        seq[j] = grid[i][j]

    if (isHappy()):
        numOfhappyseq += 1

for j in range(n):  # 각 열
    for i in range(n):  # 각 행
        seq[i] = grid[i][j]

    if (isHappy()):
        numOfhappyseq += 1

print(numOfhappyseq)  # 출력

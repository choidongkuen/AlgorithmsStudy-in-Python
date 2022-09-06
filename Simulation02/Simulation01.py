# 날짜 : 2022/09/07
# 문제 : 최고의 33위치
# 문제 설명 :
# N * N 크기의 격자 정보가 주어집니다. 이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다.
# N * N 격자를 벗어나지 않도록 3 * 3 크기의 격자를 적절하게 잘 잡아서 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.

# 입력 형식 :
# 첫 번째 줄에는 격자의 크기를 나타내는 N이 주어집니다.
# 두 번째 줄부터는 N개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며,
# 이 정보는 0또는 1로 이루어진 N개의 숫자로 나타내어지며 공백을 사이에 두고 주어집니다.
# 3 ≤ N ≤ 20

# 입력 예시 :
# 3
# 1 0 1
# 0 1 0
# 0 1 0

# 출력 예시 :
# 6


n = int(input())  # 격자의 크기
arr = [list(map(int, input().split())) for _ in range(n)]  # 동전에 대한 정보가 담긴 2차원 배열 선언


def getNumOfCoins(rowS, rowE, colS, colE):
    numOfCoins = 0
    for row in range(rowS, rowE):
        for col in range(colS, colE):
            numOfCoins += arr[row][col]

    return numOfCoins


maxCoins = 0

for i in range(n):
    for j in range(n):

        if (i + 3 > n or j + 3 > n):
            continue

        numOfCoins = getNumOfCoins(i, i + 3, j, j + 3)  # 3 x 3 구간에 존재하는 동전의 갯수 구하는 함수 호출
        maxCoins = max(maxCoins, numOfCoins)

print(maxCoins)
'''
문제
1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.

임의의 순열은 정렬을 할 수 있다. 
예를 들어  
N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다. 
첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이…

N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. 
k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄의 첫 번째 수는 소문제 번호이다. 
1인 경우 k(1 ≤ k ≤ N!)를 입력받고, 2인 경우 임의의 순열을 나타내는 N개의 수를 입력받는다. 
N개의 수에는 1부터 N까지의 정수가 한 번씩만 나타난다.

출력
k번째 수열을 나타내는 N개의 수를 출력하거나, 몇 번째 수열인지를 출력하면 된다.
'''

import math
import sys



# def getIndex() -> int:
#     val = tuple(arr[1:])
#     for i in perNArr:
#         if i == val:
#             return perNArr.index(i)

def getVal(n) -> str:
    # 답이 들어갈 배열
    answer = []
    # 인덱스 번호
    val = arr [-1]
    # 각 구간별 위치
    section = math.factorial(n)//n
    
    # 배열
    num = [i for i in range(1, n+1)]
    # 값의 길이를 만족할 때까지 반복
    while n != 1:
        if val//section > len(num):
            for i in num:
                answer.append(str(i))
            return " ".join(answer)

        answer.append(str(num.pop((val//section))))

        val = abs(val - section * (val//section))
        
        n -= 1
            
        section = math.factorial(n) // n

        if val == section:
            break

    for i in num:
        answer.append(str(i))

    return "".join(answer)


n = int(sys.stdin.readline())

nArr = [i for i in range(1,n+1)]
arr = list(map(int, sys.stdin.readline().split()))

number = arr[0]

if number == 1:
    print(getVal(n))
# else:
#     print(getIndex()+1)

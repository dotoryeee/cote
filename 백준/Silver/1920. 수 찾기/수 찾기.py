import sys
N = sys.stdin.readline().rstrip()
A = sys.stdin.readline().split()
M = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().split()

A_dict = {}

for i in A:
    A_dict[i] = 1

for num in nums:
    try:
        A_dict[num]
        print(1)
    except:
        print(0)